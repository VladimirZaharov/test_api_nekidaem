from django.db import models

from nekidaem.post.models import Post
from nekidaem.user.models import User


class Blog(models.Model):
    user = models.OneToOneField(User, unique=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
