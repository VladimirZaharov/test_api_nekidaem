from django.shortcuts import render
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet

from nekidaem.user.models import UserSubscription


class FeedsModelViewSet(ModelViewSet):
    queryset = UserSubscription.objects.get(user=UserSubscription.pk)
