from rest_framework import serializers
from posts.models import Post


class Postserializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content', 'slug', 'miniature', 'created_at', 'published', 'category']
