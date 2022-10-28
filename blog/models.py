from django.conf import settings
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self) -> str:
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=256)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')

class Comment(models.Model):
    author = models.CharField(max_length=64)
    text = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)