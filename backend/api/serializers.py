from rest_framework import serializers
from .models.models import Ability
from .models.models import Spell
from .models.models import Descriptor

class AbilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ability
        fields = '__all__'


class SpellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spell
        fields = '__all__'


class DescriptorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Descriptor
        fields = '__all__'