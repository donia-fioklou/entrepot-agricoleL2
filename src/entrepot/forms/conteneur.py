from cProfile import label
from django import forms
from django.forms import ModelForm

from entrepot.models.Conteneur import Conteneur


class ConteneurForm (ModelForm):
    class Meta:
        model=Conteneur
        fields=("IdProprietaire","numCon","typeCon")
        labels={
            
            "IdProprietaire":"Id proprietaire",
            "numCon":'Numéro conteneur',
            "typeCon":"Type du conteneur"
            
        }
        widgets={
            'IdProprietaire': forms.TextInput(attrs={'class':'form-control'}),
            'numCon': forms.TextInput(attrs={'class':'form-control'}),
            'typeCon':forms.TextInput(attrs={'class':'form-control'}),
        }