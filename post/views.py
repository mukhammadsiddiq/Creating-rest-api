from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from .models import Post
from .serializers import PostSerializer, UserSerializer
from .permissions import isAuthenticatedOrReadOnly


# Create your views here.
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (isAuthenticatedOrReadOnly, )


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer