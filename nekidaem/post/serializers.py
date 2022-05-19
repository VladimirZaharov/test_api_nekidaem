from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer

from post.models import Post


class PostModelSerializer(ModelSerializer):
    blog = StringRelatedField()
    class Meta:
        model = Post
        fields = ('__all__')