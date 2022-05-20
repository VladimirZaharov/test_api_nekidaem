import datetime
from celery import Celery
from django.core.mail import send_mail
from django.db.models import Q
from rest_framework.generics import ListAPIView

from blog.models import UserSubscription
from post.models import Post
from post.models import UserWatchedPosts
from post.serializers import PostModelSerializer

from nekidaem import settings

app = Celery()


class FeedsListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer

    def get_queryset(self, *args, **kwargs):
        subscription = UserSubscription.objects.filter(user=self.kwargs['pk']).values('subscriptions')
        user_watched_posts = UserWatchedPosts.objects.filter(user=self.kwargs['pk']).values('watched_posts')
        watched_posts_list = [p.get('watched_posts') for p in list(user_watched_posts)]
        blogs_list = [i.get('subscriptions') for i in list(subscription)]
        posts = Post.objects.filter(Q(blog__in=blogs_list) & ~Q(id__in=watched_posts_list))[0:500]
        return posts

    @staticmethod
    def mail_posts(user):
        subscription = UserSubscription.objects.filter(user=user.id).values('subscriptions')
        user_watched_posts = UserWatchedPosts.objects.filter(user=user.id).values('watched_posts')
        watched_posts_list = [p.get('watched_posts') for p in list(user_watched_posts)]
        blogs_list = [i.get('subscriptions') for i in list(subscription)]
        posts = Post.objects.filter(Q(blog__in=blogs_list) & ~Q(id__in=watched_posts_list))[0:500]
        return {i.header: i.post for i in list(posts)[-5:]}

@app.task
def send_posts_mail(user):
    title = f'Подборка постов на {datetime.datetime.now()}'
    message = f'{FeedsListAPIView.mail_posts(user)}'
    print(message)
    return send_mail(title, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)
