from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from user.models import User


class TestUserViewSet(TestCase):
    def test_get_detail(self):
        user = User.objects.create(username='Пушкин', first_name='Александр', last_name='Пушкин', email='pushkin@pushkin.ru')
        client = APIClient()
        response = client.get(f'/api/feeds/{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)