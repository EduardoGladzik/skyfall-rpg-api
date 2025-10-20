from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('habilidades', views.get_abilities),
    path('habilidade:<str:name>', views.get_ability),
    path('update:<str:name>', views.update_ability),
    path('api/', views.ability_manager),
]