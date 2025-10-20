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
    if request.method == 'GET':
        abilities = Ability.objects.all()
        serializer = AbilitySerializer(abilities, many=True)
        return Response(serializer.data)
    return Response(status=status.HTTP_400_BAD_REQUEST)