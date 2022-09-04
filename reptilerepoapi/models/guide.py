from django.db import models
from .lister import Lister

class Guide(models.Model):
    author = models.ForeignKey(Lister, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    content = models.TextField()
    publishing_date = models.DateField(auto_now_add=True)
    