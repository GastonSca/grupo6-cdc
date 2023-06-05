from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed
from django.template import loader
from django.contrib import messages
from perfil.forms import PerfilForm

# Create your views here.


def perfil(request):
    mensaje = None
    if request.method == 'POST':
        contacto_form = PerfilForm(request.POST)
       # mensaje = 'Hemos recibido tus datos'
        if contacto_form.is_valid():
            perfil = contacto_form.save()
            messages.success(request, 'Hemos recibido tus datos')
       
        else:
            messages.error(request, 'Por favor revisa los errores en el formulario')
    elif request.method == 'GET':
        contacto_form = PerfilForm()
    else:
        contacto_form = PerfilForm()
        
    context = {
        
        'perfil_form': contacto_form
    }
    
    return render(request, "perfil/perfil.html", context)
