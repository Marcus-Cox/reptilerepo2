from operator import mod
from tkinter import CASCADE
from django.db import models
from .lister import Lister
from .species import Species
from .sex import Sex
from .morph import Morph
from .diet import Diet

class Listing(models.Model):
    lister = models.ForeignKey(Lister, on_delete=models.CASCADE)
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    sex = models.ForeignKey(Sex, on_delete=models.CASCADE)
    morph = models.ForeignKey(Morph, on_delete=models.CASCADE)
    age = models.IntegerField()
    hatch_date = models.DateField(max_length=50)
    diet = models.ManyToManyField(Diet)
    
