from django import forms
from django.forms import ModelForm

from entrepot.models.Entrepot import Entrepot


class EntrepotForm (ModelForm):
    class Meta:
        model=Entrepot
        fields=("nom","adresse")
        widgets={
            'nom': forms.TextInput(attrs={'class':'form-control'}),
            'adresse': forms.TextInput(attrs={'class':'form-control'}),
        }

    