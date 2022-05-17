from django.db import models

from nekidaem.user.models import User


class Post(models.Model):
    header = models.CharField(max_length=32, blank=False)
    post = models.CharField(max_length=140)
    created_time = models.TimeField(auto_now=True)

    class Meta:
        ordering = ('created_time',)