from django.db import models


class Species(models.Model):

    species = models.CharField(max_length=50)
