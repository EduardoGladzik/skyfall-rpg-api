from django.contrib import admin
from .models.models import Ability
from .models.models import Spell
from .models.models import Descriptor

admin.site.register(Ability)
admin.site.register(Spell)
admin.site.register(Descriptor)