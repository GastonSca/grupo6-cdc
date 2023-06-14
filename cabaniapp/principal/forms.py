from django import forms
from .models import ComplejoCabanias

class ComplejoCabaniasForm(forms.ModelForm):
    class Meta:
        model = ComplejoCabanias
        fields = ['nombre']