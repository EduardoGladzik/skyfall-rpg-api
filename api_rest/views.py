from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Ability
from .serializers import AbilitySerializer

import json

@api_view(['GET'])
def get_abilities(request):
    '''
    Returns a list of all abilities. 
    '''
    if request.method == 'GET':
        abilities = Ability.objects.all()
        serializer = AbilitySerializer(abilities, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_ability(request, ability_name):
    '''
    Returns a serialized object of the requested ability. 
    '''
    if request.method == 'GET':
        try:
            ability = Ability.objects.get(pk=ability_name)
        except Ability.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = AbilitySerializer(ability)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_ability(request, ability_name):
    '''
    Updates an ability searching by url.
    '''
    if request.method == 'PUT':
        try:
            ability = Ability.objects.get(pk=ability_name)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = AbilitySerializer(ability, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def ability_manager(request):
    if request.method == 'GET':
        try:
            if request.GET['ability']:    
                ability_name = request.GET['ability']
                try:
                    ability = Ability.objects.get(pk=ability_name)
                except Ability.DoesNotExist:
                    return Response(status=status.HTTP_404_NOT_FOUND)
                serializer = AbilitySerializer(ability)
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'POST':
        new_ability = request.data
        serializer = AbilitySerializer(data=new_ability)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PUT':
        ability_name = request.data['ability_name']

        try:
            updated_ability = Ability.objects.get(pk=ability_name)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = AbilitySerializer(updated_ability, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        try:
            ability_to_delete = Ability.objects.get(pk=request.data['ability_name'])
            ability_to_delete.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)