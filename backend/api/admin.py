from django.contrib import admin
from .models.models import Ability
from .models.models import ModificationType
from .models.models import Component
from .models.models import Modification
from .models.models import Spell
from .models.models import Descriptor

admin.site.register(Ability)
admin.site.register(Spell)
admin.site.register(Descriptor)
admin.site.register(Component)
admin.site.register(Modification)
admin.site.register(ModificationType)