from rest_framework import serializers
from posts.models import Post
from users.api.serializer import UserSerializer
from categories.api.serializers import CategorySerializer


class Postserializer(serializers.ModelSerializer):
    category = CategorySerializer()
    user = UserSerializer()

    class Meta:
        model = Post
        fields = ['title', 'content', 'slug', 'miniature', 'created_at', 'user', 'published', 'category']
