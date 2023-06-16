from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotAllowed
from django.template import loader
from django.contrib import messages
from perfil.forms import PerfilForm
from .models import Perfil

# Create your views here.


def perfil(request):
    mensaje = None
    if request.method == 'POST':
        contacto_form = PerfilForm(request.POST)
       # mensaje = 'Hemos recibido tus datos'
        if contacto_form.is_valid():
            perfil = contacto_form.save()
            messages.success(request, 'Hemos recibido tus datos')
            contacto_form = PerfilForm()
        else:
            messages.error(request, 'Por favor revisa los errores en el formulario')
    elif request.method == 'GET':
        contacto_form = PerfilForm()
    else:
        contacto_form = PerfilForm()
        
    context = {
        
        'perfil_form': contacto_form
    }
    
    return render(request, "perfil/formulario_perfil.html", context)

def listar_perfiles(request):
    perfiles = Perfil.objects.all()
    return render(request, 'perfil/listar_perfiles.html', {'perfiles': perfiles})
