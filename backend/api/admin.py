from django.contrib import admin
from .models.ability import Ability
from .models.spells import Spell
from .models.ability import Descriptor

admin.site.register(Ability)
admin.site.register(Spell)
admin.site.register(Descriptor)