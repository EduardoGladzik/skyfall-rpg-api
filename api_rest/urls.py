from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.get_abilities, name='habilidades'),
 #  path('/habilidade:<str:ability_name>', views.get_ability, name='habilidade'),
]