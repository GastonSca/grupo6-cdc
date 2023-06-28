from django.shortcuts import render, redirect, get_object_or_404

from django.urls import reverse
from django.template import loader
from .forms import ComplejoCabaniasForm, CabaniasForm,ReservaForm
from django.contrib import messages
from .models import ComplejoCabanias, Servicio, Cabania,Reserva
# Create your views here.
from .forms import LoginForm, RegistroForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

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


def listar_cabaniasID(request, id):
    try:
        cabania = Cabania.objects.get(id=id)
    except Cabania.DoesNotExist:
        cabania = None
    return render(request, 'cabania/listar_cabanias.html', {'cabania': cabania})

@login_required
def reservas (request):
    reservas = Reserva.objects.all()
    vista = ''
    titulo = ''
    mensaje = None
    if request.method == 'POST':
        reserva_form = ReservaForm(request.POST)
        if reserva_form.is_valid():
            reserva_cliente = reserva_form.save()
            messages.success(request, 'Hemos recibido tus datos')
            reserva_form = ReservaForm()
        else:
            messages.error(request, 'Por favor revisa los errores en el formulario')
    elif request.method == 'GET':
        reserva_form= ReservaForm()
    else:
        reserva_form = ReservaForm()
        
    context = {
        'reserva_form': reserva_form,
        'reservas': reservas
    }
    
    return render(request,'reservas/reserva.html',context)

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            
            username = form.cleaned_data['usuario']
            password = form.cleaned_data['contraseña'] 
            user = authenticate(request, username=username, password=password)
            if user is not None:
                return render(request, 'login/login.html', {'mensaje': 'Inicio de sesión correctoooo'})
            else:
                return render(request, 'login/login.html', {'mensaje': 'Inicio de sesión erroneo'})
            # Realizar lógica de autenticación
            # ...
                
    else:
        form = LoginForm()
    
    return render(request, 'login/login.html', {'form': form})


def logout_view(request):
    logout(request)