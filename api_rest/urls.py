from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('habilidades', views.get_abilities),
    path('habilidade:<str:ability_name>', views.get_ability),
]