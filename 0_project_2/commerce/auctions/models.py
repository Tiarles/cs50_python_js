from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    def __str__(self):
        return f"{self.username}, {self.email}"


class Listing(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=1000)
    starting_bid = models.FloatField()
    category = models.CharField(max_length=64)
    url_image = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.title} ($ {self.starting_bid})"

