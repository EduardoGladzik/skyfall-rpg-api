from django.db import models

class Ability(models.Model):

    source = models.CharField(max_length=50, default='',)
    execution_type = models.TextChoices('Ação', 'Ação Bonus', 'Reação', 'Ação Livre', 'Passiva', 'Mais que uma Ação')
    name = models.CharField(primary_key=True, max_length=50, default='')
    cost = models.IntegerField(default=0)
    descriptors = models.CharField(max_length=50, default='') # Procurar maneiras de criar uma lista de opções onde seja possível adicionar mais de uma opção à variável
    description = models.TextField(default='')

    range = models.CharField(max_length=50, default='')
    target = models.CharField(max_length=50, default='')
    duration = models.TextChoices('Instantânea', 'Concentração')
    attack = models.CharField(max_length=50, default='')
    trigger = models.CharField(max_length=50, default='')

    hit = models.TextField(default='')
    miss = models.TextField(default='')
    effect = models.TextField(default='')
    special = models.TextField(default='')

    # Adicionar modificações
    
def __str__():
    return f"{Ability.name} {Ability.cost} PE"