from django.contrib import admin
from .models.ability import Ability
from .models.spells import Spell

admin.site.register(Ability)
admin.site.register(Spell)