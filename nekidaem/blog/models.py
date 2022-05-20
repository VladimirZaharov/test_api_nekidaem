from django.db import models

from user.models import User


class Blog(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class UserSubscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subscriptions = models.ForeignKey(Blog, on_delete=models.CASCADE)