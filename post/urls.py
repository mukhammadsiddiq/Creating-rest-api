from django.urls import path
from .views import ListApiPostView, UpdateApiPostView

urlpatterns = [
    path('api/<int:pk>/', UpdateApiPostView.as_view()),
    path('api/', ListApiPostView.as_view()),
]