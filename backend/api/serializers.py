from rest_framework import serializers
from .models.models import Ability
from .models.models import Spell
from .models.models import Descriptor

class AbilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ability
        fields = '__all__'
    
    def to_representation(self, instance):
        if isinstance(instance, Spell):
            return SpellSerializer(instance).data

        spell_obj = getattr(instance, 'spell', None)
        if spell_obj is not None:
            return SpellSerializer(spell_obj).data
        return super().to_representation(instance)


class SpellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spell
        fields = '__all__'


class DescriptorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Descriptor
        fields = '__all__'