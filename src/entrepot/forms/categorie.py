from django import forms
from django.forms import ModelForm

from entrepot.models.Categorie import Categorie


class CategorieForm (ModelForm):
    class Meta:
        model=Categorie
        fields=("nom",)
        widgets={
            'nom': forms.TextInput(attrs={'class':'form-control'}),
        }
    