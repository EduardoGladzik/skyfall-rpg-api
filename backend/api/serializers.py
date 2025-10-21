from rest_framework import serializers
from .models.ability import Ability
from .models.spells import Spell
from .models.ability import Descriptor

class AbilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ability
        fields = '__all__'

class SpellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spell
        fields = '__all__'


class SpellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Descriptor
        fields = '__all__'