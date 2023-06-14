from django.contrib import admin
from django.urls import path
from . import views
#from .views import crear_complejo

urlpatterns = [
    path('', views.index, name='index'),
    path('crear_complejo/', views.crear_complejo, name='crear_complejo'),
]