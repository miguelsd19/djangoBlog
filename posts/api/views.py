from rest_framework.viewsets import ModelViewSet
from posts.models import Post
from posts.api.serializers import Postserializer
from posts.api.permissions import IsAdminOrReadOnly


class PostApiviewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = Postserializer
    queryset = Post.objects.filter(published=True)
    lookup_field = 'slug'
