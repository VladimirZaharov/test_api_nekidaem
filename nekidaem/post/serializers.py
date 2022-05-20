from rest_framework import serializers
from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer

from post.models import Post

from blog.models import Blog

from user.models import User


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')

class BlogModelSerializer(ModelSerializer):
    blog = serializers.StringRelatedField(many=True)
    class Meta:
        model = Blog
        fields = ('__all__')


class PostModelSerializer(ModelSerializer):
    blog = BlogModelSerializer

    class Meta:
        model = Post
        fields = ('__all__')
