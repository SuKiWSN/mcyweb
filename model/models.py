from django.db import models

class user(models.Model):
    address = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class favorite(models.Model):
    address = models.CharField(max_length=255)
    videoId = models.IntegerField()
    videoTitle = models.CharField(max_length=255)
    ImageUrl = models.CharField(max_length=255)
    price = models.IntegerField()