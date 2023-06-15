from django.contrib import admin
from django.urls import path
from . import views
#from .views import crear_complejo

urlpatterns = [
    path('', views.index, name='index'),
    path('crear_complejo/', views.crear_complejo, name='crear_complejo'),
    path('listar_complejos/', views.listar_complejos, name='listar_complejos'),
    path('nueva_cabania/', views.crear_cabania, name='nueva_cabania'),
    path('listar_cabanias/', views.listar_cabanias, name='listar_cabanias'),
]