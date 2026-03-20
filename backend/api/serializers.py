from rest_framework import serializers
from .models.models import Ability
from .models.models import Spell
from .models.models import Descriptor
    
class AbilitySerializer(serializers.ModelSerializer):
    
    descriptors = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )
    class Meta:
        model = Ability
        fields = '__all__'


class SpellSerializer(serializers.ModelSerializer):
    
    components = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )
    
    descriptors = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )
    class Meta:
        model = Spell
        fields = '__all__'


class DescriptorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Descriptor
        fields = '__all__'