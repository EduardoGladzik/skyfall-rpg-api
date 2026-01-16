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