from django import forms
import re
from django.forms import ValidationError

def validar_dni(value):
    if len(value) != 8:
        raise forms.ValidationError('El DNI debe tener 8 dígitos')
    try:
        int(value)
    except ValueError:
        raise ValidationError('El DNI solo debe contener números')


def solo_caracteres(value):
    if any(char.isdigit() for char in value):
        raise ValidationError('El nombre no puede contener números. %(valor)s',
                              code='Invalid',
                              params={'valor': value})


def validar_telefono(value):
    patron = r'^\d{2}-\d{8}$'
    if not re.match(patron, value):
        raise forms.ValidationError('Número de teléfono inválido')




class PerfilForm(forms.Form):
    nombre = forms.CharField(label='Nombre')
    apellido = forms.CharField(label='Apellido')
    dni = forms.CharField(label='Dni')
    fecha_nacimiento = forms.DateField(label='Nacimiento')
    telefono = forms.CharField(label='Telefono')
   
    nombre = forms.CharField(
        label='Nombre',
        max_length=50,
        validators=(solo_caracteres,),
        widget=forms.TextInput(
            attrs={'class': 'datos',
                   'placeholder': 'Solo letras',
                   'for':"apellidoAdmin",
                   'id':'lblNombAdmin'}
        )
    )
   
      
    apellido = forms.CharField(
        label='Apellido',
        max_length=50,
        validators=(solo_caracteres,),
        widget=forms.TextInput(
            attrs={'class': 'datos',
                   'placeholder': 'Solo letras',
                   'for' :"apellidoAdmin",
                   'id':'lblApellidoAdmin'}
        )
    )
    fecha_nacimiento = forms.DateField(
        label='Fecha de Nacimiento',
        widget=forms.DateInput(attrs={'class': 'datos', 'placeholder': 'DD-MM-YYYY'})
    )
    
 
    dni = forms.CharField(
    label='Dni',
    widget=forms.TextInput(
        attrs={'class': 'datos', 'placeholder': 'Dni' , 'for':'dniAdmin', 'id':'lblApellidoAdmin'}
    ),
    validators=(validar_dni,),
)

    telefono = forms.CharField(
        label='Telefono',
        required=False,
        validators=(validar_telefono,),
        widget=forms.TextInput(attrs={'class': 'datos',
                                    'placeholder': 'cod Area- Numero'})
    )
'''
    def clean_mensaje(self):
        data = self.cleaned_data['mensaje']
        if len(data) < 10:
            raise ValidationError(
                "Debes especificar mejor el mensaje que nos envias")
        return data

    def clean(self):
        cleaned_data = super().clean()
        asunto = cleaned_data.get("asunto")
        suscripcion = cleaned_data.get("suscripcion")

        if suscripcion and asunto and "suscripcion" not in asunto:
            msg = "Debe agregar la palabara 'suscripcion' al asunto."
            self.add_error('asunto', msg)'''