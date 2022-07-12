from django import forms
from django.forms import ModelForm

from entrepot.models.Fournisseur import Fournisseur


class FournisseurForm (ModelForm):
    class Meta:
        model=Fournisseur
        fields=("nom","contact","email","adresse")
        widgets={
            'nom': forms.TextInput(attrs={'class':'form-control'}),
            'contact': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'adresse': forms.Textarea(attrs={'class':'form-control'})
        }
    