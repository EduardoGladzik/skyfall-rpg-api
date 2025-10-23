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
        ability_serializer = AbilitySerializer(Ability.objects.all().select_related('spell'), many=True)
        return Response(ability_serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_ability(request, name):
    '''
    Returns a serialized object of the requested ability. 
    '''
    if request.method == 'GET':
        object = request.data
        if object.__contains__('descriptor'):
            object = Descriptor.objects.get(pk=name)
            serializer = DescriptorSerializer(object)
        elif object.__contains__('layers'):
            object = Spell.objects.get(pk=name)
            serializer = SpellSerializer(object)
        else:
            object = Ability.objects.get(pk=name)
            serializer = AbilitySerializer(object)
        
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def ability_manager(request):
    if request.method == 'GET':
        try:
            if request.GET['ability']:    
                name = request.GET['ability']
                try:
                    ability = Ability.objects.get(pk=name)
                except Ability.DoesNotExist:
                    return Response(status=status.HTTP_404_NOT_FOUND)
                serializer = AbilitySerializer(ability)
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'POST':
        new_entry = request.data
        if new_entry.keys().__contains__('layers'):
            serializer = SpellSerializer(data=new_entry)
        elif new_entry.keys().__contains__('descriptor'):
            serializer = DescriptorSerializer(data=new_entry)
        else:
            serializer = AbilitySerializer(data=new_entry)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
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