from django.db import models

class Ability(models.Model):

    ability_source = models.CharField(max_length=50, default='',)
    ability_execution_type = models.TextChoices('Ação', 'Ação Bonus', 'Reação', 'Ação Livre', 'Passiva', 'Mais que uma Ação')
    ability_name = models.CharField(primary_key=True, max_length=50, default='')
    ability_cost = models.IntegerField(default=0)
    ability_descriptors = models.CharField(max_length=50, default='') # Procurar maneiras de criar uma lista de opções onde seja possível adicionar mais de uma opção à variável
    ability_description = models.TextField(default='')

    ability_range = models.CharField(max_length=50, default='')
    ability_target = models.CharField(max_length=50, default='')
    ability_duration = models.TextChoices('Instantânea', 'Concentração')
    ability_attack = models.CharField(max_length=50, default='')
    ability_trigger = models.CharField(max_length=50, default='')

    ability_hit = models.TextField(default='')
    ability_miss = models.TextField(default='')
    ability_effect = models.TextField(default='')
    ability_special = models.TextField(default='')

    # Adicionar modificações
    
    def __str__(self):
        return f"{self.ability_name} {self.ability_cost} PE"