from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models.ability import Ability
from .serializers import AbilitySerializer
from .models.spells import Spell
from .serializers import SpellSerializer

import json

@api_view(['GET'])
def get_abilities(request):
    '''
    Returns a list of all abilities. 
    '''
    if request.method == 'GET':
        list = []
        if Ability.objects.exists():
            for ability in Ability.objects.all():
                if not ability.descriptors.__contains__('Mágico'):
                    list.append(ability)
        ability_serializer = AbilitySerializer(list, many=True)
        spell_serializer = SpellSerializer(Spell.objects.all(), many=True)


        return Response(ability_serializer.data + spell_serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_ability(request, name):
    '''
    Returns a serialized object of the requested ability. 
    '''
    if request.method == 'GET':
        try:
            ability = Ability.objects.get(pk=name)
        except Ability.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        if ability.descriptors.__contains__('Mágico'):
            ability = Spell.objects.get(pk=name)
            serializer = SpellSerializer(ability)
        else:
            serializer = AbilitySerializer(ability)

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
        if new_entry.keys().__contains__('components'):
            serializer = SpellSerializer(data=new_entry)
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