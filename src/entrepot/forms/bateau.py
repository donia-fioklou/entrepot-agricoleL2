
from django import forms
from django.forms import ModelForm
from entrepot.models.Bateau import Bateau



class BateauForm (ModelForm):
    class Meta:
        model=Bateau
        fields=("nom","immatriculation")
        labels={
            "nom":'Nom',
            "immatriculation":'immatriculation'
        }
        widgets={
            'nom': forms.TextInput(attrs={'class':'form-control'}),
            'immatriculation': forms.TextInput(attrs={'class':'form-control'}),
        }