from django.shortcuts import render

from django.urls import reverse
from django.template import loader
from principal.forms import ComplejoCabaniasForm
# Create your views here.

def index(request):
    return render(request,"principal/index.html",{})



def crear_complejo(request):
    if request.method == 'POST':
        form = ComplejoCabaniasForm(request.POST)
        if form.is_valid():
            # Procesa los datos del formulario
            nombre = form.cleaned_data['nombre']
            direccion = form.cleaned_data['direccion']
            # Realiza las acciones necesarias con los datos del formulario

    else:
        form = ComplejoCabaniasForm()

    return render(request, 'complejo/formulario_complejo.html', {'form': form})