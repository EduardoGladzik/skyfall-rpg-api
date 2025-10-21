from django.db import models

class Ability(models.Model):

    SOURCE_OPTIONS = [
        ('Livro Básico', 'Livro Básico'),
    ]

    EXECUTION_OPTIONS = [
        ('Ação', 'Ação'), 
        ('Ação Bonus', 'Ação Bonus'), 
        ('Reação', 'Reação'), 
        ('Ação Livre', 'Ação Livre'), 
        ('Passiva', 'Passiva'), 
        ('Mais que uma Ação', 'Mais que uma Ação')
    ]

    DURATION_OPTIONS = [
        ('Instantânea', 'Instantânea'),
        ('Concentração', 'Concentração'),
    ]

    source = models.CharField(max_length=50, choices=SOURCE_OPTIONS, default='Livro Básico',)
    execution_type = models.CharField(max_length=20, choices=EXECUTION_OPTIONS, default='Ação')
    name = models.CharField(primary_key=True, max_length=50, default='')
    cost = models.SmallIntegerField(default=0)
    descriptors = models.CharField(max_length=50, default='')
    description = models.TextField(default='', null=True, blank=True)

    range = models.SmallIntegerField(default=0)
    target = models.CharField(max_length=50, default='')
    duration = models.CharField(max_length=20, choices=DURATION_OPTIONS, default='Instantânea')
    attack = models.CharField(max_length=50, default='', null=True, blank=True)
    trigger = models.CharField(max_length=50, default='', null=True, blank=True)

    hit = models.TextField(default='', null=True, blank=True)
    miss = models.TextField(default='', null=True, blank=True)
    effect = models.TextField(default='')
    special = models.TextField(default='', null=True, blank=True)

    # Adicionar modificações
    
def __str__():
    return f"{Ability.name} {Ability.cost} PE"