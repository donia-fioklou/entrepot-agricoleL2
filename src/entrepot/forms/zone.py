from django import forms
from django.forms import ModelForm

from entrepot.models.Zone import Zone


class ZoneForm (ModelForm):
    class Meta:
        model=Zone
        fields=("nom","entrepot","qteMax","qteActu")
        labels={
            "qteMax":"quantité maximale",
            "qteActu":"quantité actuelle",
            
        }
        widgets={
            'nom': forms.TextInput(attrs={'class':'form-control'}),
            'entrepot':forms.Select(attrs={'class':'form-control'}),
            'qteMax': forms.TextInput(attrs={'class':'form-control'}),
            'qteActu': forms.TextInput(attrs={'class':'form-control'}),
            
            
        }

    