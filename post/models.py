from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.TimeField(auto_now=True)
    update = models.TimeField(auto_now=True)

    def __str__(self):
        return self.title