from django.shortcuts import render

from django.urls import reverse
from django.template import loader

# Create your views here.

def index(request):
    return render(request,"principal/index.html",{})