from cProfile import label
from django import forms
from django.forms import ModelForm

from entrepot.models.Conteneur import Conteneur


class ConteneurForm (ModelForm):
    class Meta:
        model=Conteneur
        fields=("numCon",)
        labels={
            "numCon":'Numéro',
        }
        widgets={
            'numCon': forms.TextInput(attrs={'class':'form-control'}),
        }