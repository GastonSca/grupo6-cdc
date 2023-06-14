from django import forms

class ComplejoCabaniasForm(forms.Form):
    id = forms.CharField(max_length=5)
    nombre = forms.CharField(max_length=100)