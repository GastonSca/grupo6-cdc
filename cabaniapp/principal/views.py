from django.shortcuts import render, redirect

from django.urls import reverse
from django.template import loader
from .forms import ComplejoCabaniasForm, CabaniasForm
from django.contrib import messages
from .models import ComplejoCabanias, Servicio, Cabania
# Create your views here.

def index(request):
    return render(request,"principal/index.html",{})

# Vistas para complejo
def crear_complejo(request):
    if request.method == 'POST':
        form = ComplejoCabaniasForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda los datos en la base de datos
            
            return redirect('../')  # Redirecciona a una página de éxito o a donde desees
        else:
            form.nombre.errors='No puede tener más de 100 caracteres'

    else:
        form = ComplejoCabaniasForm()

    return render(request, 'complejo/formulario_complejo.html', {'form': form})

def listar_complejos(request):
    complejos = ComplejoCabanias.objects.all()
    return render(request, 'complejo/listar_complejos.html', {'complejos': complejos})


# Vistas para cabanias
def crear_cabania(request):
    if request.method == 'POST':
        form = CabaniasForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda los datos en la base de datos
            
            return redirect('../')  # Redirecciona a una página de éxito o a donde desees
        else:
            form.nombre.errors='No puede tener más de 100 caracteres'

    else:
        form = CabaniasForm()

    return render(request, 'cabania/formulario_cabania.html', {'form': form})


def listar_cabanias(request):
    cabanias = Cabania.objects.all()
    return render(request, 'cabania/listar_cabanias.html', {'cabanias': cabanias})