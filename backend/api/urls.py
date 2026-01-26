from django.urls import path

from . import views

urlpatterns = [
    path('habilidades', views.get_abilities),
    path('habilidades/<str:name>', views.get_ability),
    path('magias', views.get_spells),
    path('magias/<str:name>', views.get_spell),
    path('descritores', views.get_descriptors),
    path('descritores/<str:name>', views.get_descriptor),
]