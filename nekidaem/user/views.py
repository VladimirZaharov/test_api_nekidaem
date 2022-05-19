from django.db.models import Q
from rest_framework.viewsets import ModelViewSet
from django.views.generic.list import ListView

from blog.models import UserSubscription
from post.models import Post
from post.models import UserWatchedPosts
from blog.models import Blog

from post.serializers import PostModelSerializer


class FeedsModelViewSet(ModelViewSet):
    # blog = Blog.objects.all()
    # feeds = UserSubscription.objects.all()
    # queryset = Post.objects.filter(Q(pk__in=feeds.subscriptions) & ~Q(pk__in=UserWatchedPosts.watched_posts) & Q())
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer
