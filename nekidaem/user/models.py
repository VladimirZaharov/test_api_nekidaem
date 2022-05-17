from django.contrib.auth.models import AbstractUser
from django.db import models

from nekidaem.blog.models import Blog


class User(AbstractUser):
    pass


class UserSubscription(models.Model):
    user = models.OneToOneField(User, unique=True)
    subscriptions = models.ForeignKey(Blog, on_delete=models.CASCADE)
