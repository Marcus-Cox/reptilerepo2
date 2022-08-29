from django.db import models
from django.contrib.auth.models import User


class Lister(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=50)
    date_joined = models.DateField(auto_now_add=True)