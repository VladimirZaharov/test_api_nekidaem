from django.db import models

from nekidaem.user.models import User


class UserBlog(models.Model):
    user = models.OneToOneField(User, unique=True)
    header = models.CharField(max_length=32, blank=False)
    post = models.CharField(max_length=140)
    created_time = models.TimeField(auto_now=True)
