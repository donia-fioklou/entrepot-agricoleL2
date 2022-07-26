from django import forms
from django.forms import ModelChoiceField, ModelForm
from entrepot.models.Fournisseur import Fournisseur
from entrepot.models.LigneReception import LigneReception
from entrepot.models.Produit import Produit
from entrepot.models.Zone import Zone

from entrepot.models.Reception import Reception



class RecepForm (ModelForm):
    class Meta:
        model=Reception
        fields=("nomRecep","dateRecep","fournisseur", "produit",)
        widgets={
            'nomRecep': forms.TextInput(attrs={'class':'form-control'}),
            'dateRecep': forms.DateInput(attrs={'class':'form-control'}),
            'fournisseur': forms.Select( attrs={'class':'form-control'}),
            'produit': forms.Select(attrs={'class':'form-control'}),
        }


class LigneRecepForm (ModelForm):
    class Meta:
        model=LigneReception
        fields=("qteProd","numLot",)
        widgets={
            'qteProd': forms.TextInput(attrs={'class':'form-control'}),
            'numLot': forms.TextInput(attrs={'class':'form-control'}),
            
            
        }

    