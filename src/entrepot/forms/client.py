from django import forms
from django.forms import ModelForm

from entrepot.models.Client import Client


class ClientForm (ModelForm):
    class Meta:
        model=Client
        fields=("nom","contact","email","adresse")
        widgets={
            'nom': forms.TextInput(attrs={'class':'form-control'}),
            'contact': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'adresse': forms.TextInput(attrs={'class':'form-control'}),
        }

    