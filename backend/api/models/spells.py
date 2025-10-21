from django.db import models
from .ability import Ability

class Spell(Ability):
    category = models.CharField(max_length=20, default='')
    level = models.CharField(max_length=20, default='')
    components = models.CharField(max_length=20, default='')

def __str__():
    return f"{Ability.name}"