from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from .models import Post
from .serializers import PostSerializer, UserSerializer
from .permissions import isAuthenticatedOrReadOnly


# Create your views here.


class ListApiPostView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UpdateApiPostView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (isAuthenticatedOrReadOnly, )


class UserListApiView(ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserUpdateApiView(RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer