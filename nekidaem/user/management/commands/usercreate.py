import random

from django.core.management.base import BaseCommand
from django.db.models import Q
from faker import Faker

from user.models import User
from blog.models import Blog
from blog.models import UserSubscription

fake = Faker()

class Command(BaseCommand):
    def handle(self, *args, **options):
        users = User.objects.all()
        blog = Blog.objects.all()
        subscriptions = UserSubscription.objects.all()
        subscriptions.delete()
        blog.delete()
        users.delete()
        users_number = int(input('Введите количество пользователей: '))
        subscriptions_number = int(input('Введите макс количество подписчиков:'))
        for i in range(users_number):
            user = User.objects.create(
                username=fake.name(),
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.email()
            )
            user.save()
            blog = Blog.objects.create(user=user)
            blog.save()

        for user in users:
            for s in range(random.randint(1, subscriptions_number)):
                blogs = Blog.objects.filter(~Q(user=user))
                users_subscriptions = UserSubscription.objects.create(
                    user=user,
                    subscriptions=fake.random_element(blogs)
                )
                users_subscriptions.save()
        superuser = User.objects.create(
            username='root',
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email()
        )
        superuser.is_superuser = True
        superuser.password = 'root'
        superuser.save()