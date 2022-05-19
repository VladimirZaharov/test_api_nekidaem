from django.db import models

from blog.models import Blog

from user.models import User


class Post(models.Model):
    header = models.CharField(max_length=32, blank=False)
    post = models.CharField(max_length=140)
    created_time = models.TimeField(auto_now=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    class Meta:
        ordering = ('created_time',)


class UserWatchedPosts(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    watched_posts = models.ForeignKey(Post, on_delete=models.CASCADE)