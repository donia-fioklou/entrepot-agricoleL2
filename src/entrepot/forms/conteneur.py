from cProfile import label
from django import forms
from django.forms import ModelForm

from entrepot.models.Conteneur import Conteneur


class ConteneurForm (ModelForm):
    class Meta:
        model=Conteneur
        fields=("IdProprietaire","numCon","typeCon","bateau")
        labels={
            
            "IdProprietaire":"Id proprietaire",
            "numCon":'Numéro conteneur',
            "typeCon":"Type du conteneur",
            "bateau":"Bateau"
            
        }
        widgets={
            'IdProprietaire': forms.TextInput(attrs={'class':'form-control'}),
            'numCon': forms.TextInput(attrs={'class':'form-control'}),
            'typeCon':forms.TextInput(attrs={'class':'form-control'}),
            'bateau':forms.Select(attrs={'class':'form-control'})
        }