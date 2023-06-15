from django import forms
from .models import ComplejoCabanias, Cabania, Servicio

class ComplejoCabaniasForm(forms.ModelForm):
    class Meta:
        model = ComplejoCabanias
        fields = ['nombre']


class CabaniasForm(forms.ModelForm):
    servicios = forms.ModelMultipleChoiceField(queryset=Servicio.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Cabania
        fields = ['idComplejo', 'nombre', 'servicios', 'cantDormitorios', 'cantPersonas']