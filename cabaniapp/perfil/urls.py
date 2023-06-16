from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('crear_perfil', views.perfil, name='crear_perfil'),
    path('listar_perfiles', views.listar_perfiles, name='listar_perfiles'),
]
