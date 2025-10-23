from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models.models import Ability
from .serializers import AbilitySerializer
from .models.models import Spell
from .serializers import SpellSerializer
from .models.models import Descriptor
from .serializers import DescriptorSerializer

import json

@api_view(['GET'])
def get_abilities(request):
    '''
    Returns a list of all abilities. 
    ''' 
    if request.method == 'GET':
        serializer = AbilitySerializer(Ability.objects.all(), many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_ability(request, name):
    '''
    Returns a serialized object of the requested ability. 
    '''
    if request.method == 'GET':
        serializer = AbilitySerializer(Ability.objects.get(pk=name))
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_spells(request):
    '''
    Returns a list of all spells. 
    ''' 
    if request.method == 'GET':
        serializer = SpellSerializer(Spell.objects.all(), many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_descriptors(request):
    '''
    Returns a list of all descriptors. 
    ''' 
    if request.method == 'GET':
        serializer = DescriptorSerializer(Descriptor.objects.all(), many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_descriptor(request, name):
    '''
    Returns a serialized object of the requested descriptor. 
    '''
    if request.method == 'GET':
        serializer = DescriptorSerializer(Descriptor.objects.get(pk=name))
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST', 'PUT', 'DELETE'])
def ability_manager(request):
    '''
    These are just temporary methods for me to manage tests using insomnia.
    '''
    if request.method == 'POST':
        new_entry = request.data
        if Spell.is_spell(new_entry):
            serializer = SpellSerializer(data=new_entry)
        else:
            serializer = AbilitySerializer(data=new_entry)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    if request.method == 'PUT':

        name = request.data['name']
        try:
            updated_ability = Ability.objects.get(pk=name)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = AbilitySerializer(updated_ability, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        try:
            to_delete = Ability.objects.get(pk=request.data['name'])
            to_delete.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)