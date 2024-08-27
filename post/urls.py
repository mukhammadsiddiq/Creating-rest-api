from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import PostViewSet, UserViewSet


router = SimpleRouter()
router.register('user', UserViewSet, basename='users')
router.register('', PostViewSet, basename='posts')

urlpatterns = router.urls
