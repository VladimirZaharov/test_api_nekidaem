from django.core.management.base import BaseCommand
from faker import Faker

from user.models import User

from blog.models import Blog

fake = Faker()

class Command(BaseCommand):
    def handle(self, *args, **options):
        users = User.objects.all()
        blog = Blog.objects.all()
        blog.delete()
        users.delete()
        users_number = int(input(': '))
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
        superuser = User.objects.create(
            username='root',
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email()
        )
        superuser.is_superuser = True
        superuser.password = 'root'
        superuser.save()