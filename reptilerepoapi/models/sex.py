from django.db import models


class Sex(models.Model):

    sex = models.CharField(max_length=50)
    
