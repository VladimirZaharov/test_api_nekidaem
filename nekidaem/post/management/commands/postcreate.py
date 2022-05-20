import random

from django.core.management.base import BaseCommand
from faker import Faker

from post.models import Post

from blog.models import Blog

fake = Faker()

class Command(BaseCommand):
    def handle(self, *args, **options):
        blogs = Blog.objects.all()

        users = Post.objects.all()
        users.delete()
        posts_number = int(input('Введите максимальное число постов у пользователя: '))
        for blog in blogs:
            for i in range(random.randint(1, posts_number)):
                post = Post.objects.create(
                    header=fake.text(max_nb_chars=10),
                    post=fake.text(max_nb_chars=100),
                    blog=blog,
                )
                post.save()
