from django.db import models
from .ability import Ability

class Spell(Ability):

    CATEGORY_OPTIONS = [
        ('Controle', 'Controle'),
        ('Ofensivo', 'Ofensivo'),
        ('Utilitário', 'Utilitário'),
    ]

    LAYER_OPTIONS = [
        ('Truque', 'Truque'),
        ('Superficial', 'Superficial'),
        ('Rasa', 'Rasa'),
        ('Profunda', 'Profunda'),
    ]

    category = models.CharField(max_length=20, choices=CATEGORY_OPTIONS, default='Controle')
    layer = models.CharField(max_length=20, choices=LAYER_OPTIONS, default='Truque')
    components = models.CharField(max_length=20, default='')

def __str__():
    return f"{Ability.name}"