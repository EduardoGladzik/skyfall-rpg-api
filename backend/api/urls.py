from django.urls import path

from . import views

urlpatterns = [
    path('habilidades', views.get_abilities),
    path('habilidade:<str:name>', views.get_ability),
    path('magias', views.get_spells),
    path('magia:<str:name>', views.get_ability),
    path('descritores', views.get_descriptors),
    path('descritor:<str:name>', views.get_descriptor),
    path('habilidades/controlador', views.ability_manager) # Temporary path for testing ability creation
]