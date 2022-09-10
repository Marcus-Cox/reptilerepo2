from django.db import models
from .listing import Listing
from .diet import Diet

class ReptileDiet(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    diet = models.ForeignKey(Diet, on_delete=models.CASCADE)
