from django.shortcuts import render, redirect

from django.urls import reverse
from django.template import loader
from .forms import ComplejoCabaniasForm
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request,"principal/index.html",{})


def crear_complejo(request):
    if request.method == 'POST':
        form = ComplejoCabaniasForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda los datos en la base de datos
            return redirect('../principal/')  # Redirecciona a una página de éxito o a donde desees

    else:
        form = ComplejoCabaniasForm()

    return render(request, 'complejo/formulario_complejo.html', {'form': form})
