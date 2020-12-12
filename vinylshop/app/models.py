from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

UserModel = get_user_model()


class Album(models.Model):
    artist_name = models.CharField(max_length=50)
    album_name = models.CharField(max_length=50)
    image = models.ImageField(default=None)
    description = models.TextField(max_length=1000)
    price = models.FloatField()


class Profile(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    phone = models.CharField(max_length=15)


class Comment(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    bid_price = models.FloatField(default=None)
    comment = models.TextField(max_length=100, default=None)
