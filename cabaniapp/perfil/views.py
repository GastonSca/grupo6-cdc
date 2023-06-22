from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotAllowed
from django.template import loader
from django.contrib import messages
from perfil.forms import PerfilForm
from  perfil.forms import PerfilClienteForm
from .models import Perfil
from .models import PerfilCliente

# Create your views here.


def perfil(request):
    perfil_vista = ''
    titulo_perfil = ''
    mensaje = None
    perfiles = Perfil.objects.all()
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
        perfil_vista = request.GET.get('vista')
        titulo_perfil = request.GET.get('titulo')
    else:
        contacto_form = PerfilForm()
        
    context = {
        
        'perfil_form': contacto_form,
        'tipo_perfil': perfil_vista,
        'titulo_perfil': titulo_perfil,
        'perfiles': perfiles
    }
    
    return render(request, "perfil/formulario_perfil.html", context)

def listar_perfiles(request):
    perfiles = Perfil.objects.all()
    return render(request, 'perfil/listar_perfiles.html', {'perfiles': perfiles})

def perfil_cliente(request):
    perfiles = PerfilCliente.objects.all()
    perfil_vista = ''
    titulo_perfil = ''
    mensaje = None
    if request.method == 'POST':
        perfil_cliente_form = PerfilClienteForm(request.POST)
        if perfil_cliente_form.is_valid():
            perfil_cliente = perfil_cliente_form.save()
            messages.success(request, 'Hemos recibido tus datos')
            perfil_cliente_form = PerfilClienteForm()
        else:
            messages.error(request, 'Por favor revisa los errores en el formulario')
    elif request.method == 'GET':
        perfil_cliente_form = PerfilClienteForm()
        perfil_vista = request.GET.get('vista')
        titulo_perfil = request.GET.get('titulo')
    else:
        perfil_cliente_form = PerfilClienteForm()
        
    context = {
        'perfil_form': perfil_cliente_form,
        'tipo_perfil': perfil_vista,
        'titulo_perfil': titulo_perfil,
        'perfiles': perfiles
    }
    
    return render(request, "perfil/formulario_perfil.html", context)

