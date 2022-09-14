from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from posts.models import Post
from posts.api.serializers import Postserializer
from posts.api.permissions import IsAdminOrReadOnly


class PostApiviewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = Postserializer
    queryset = Post.objects.filter(published=True)
    lookup_field = 'slug'

    #Filtrado por categoria por id
    filter_backends = [DjangoFilterBackend]
    #filterset_fields = ['category']
    #Por slug
    filterset_fields = ['category__slug']
    #Por slug o id
    # filterset_fields = ['category', 'category__slug']
