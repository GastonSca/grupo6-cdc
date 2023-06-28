from django import forms
from .models import ComplejoCabanias, Cabania, Servicio ,Reserva, Usuario

class ComplejoCabaniasForm(forms.ModelForm):
    class Meta:
        model = ComplejoCabanias
        fields = ['nombre']


class CabaniasForm(forms.ModelForm):
    servicios = forms.ModelMultipleChoiceField(queryset=Servicio.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Cabania
        fields = ['idComplejo', 'nombre', 'servicios', 'cantDormitorios', 'cantPersonas']




class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['id_complejo', 'id_cabania', 'cliente', 'fecha_entrada', 'fecha_salida']


class LoginForm(forms.Form):
    usuario = forms.CharField(label='usuario', max_length=100)
    contraseña = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'usuario', 'contraseña']
        widgets = {
            'contraseña': forms.PasswordInput()
        }