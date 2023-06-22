from django import forms
from .models import ComplejoCabanias, Cabania, Servicio ,Reserva

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
