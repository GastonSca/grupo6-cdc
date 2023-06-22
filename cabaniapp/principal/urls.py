from django.contrib import admin
from django.urls import path
from . import views
#from .views import crear_complejo

urlpatterns = [
    path('', views.index, name='index'),
    path('crear_complejo/', views.crear_complejo, name='crear_complejo'),
    path('listar_complejos/', views.listar_complejos, name='listar_complejos'),
    path('crear_cabania/', views.crear_cabania, name='crear_cabania'),
    path('listar_cabanias/', views.listar_cabanias, name='listar_cabanias'),
    path('reservas/', views.reservas, name='reservas'),
    path('listar_cabanias/<int:id>/', views.listar_cabaniasID, name='listar_cabaniasID'),
]