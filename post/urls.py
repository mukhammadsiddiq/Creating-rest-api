from django.urls import path
from .views import ListApiPostView, UpdateApiPostView, UserListApiView, UserUpdateApiView

urlpatterns = [
    path('user/', UserListApiView.as_view()),
    path('user/<int:pk>', UserUpdateApiView.as_view()),
    path('api/<int:pk>/', UpdateApiPostView.as_view()),
    path('api/', ListApiPostView.as_view()),
]