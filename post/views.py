from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from .models import Post
from .serializers import PostSerializer
# Create your views here.


class ListApiPostView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UpdateApiPostView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer