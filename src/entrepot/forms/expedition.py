
from cProfile import label
from tkinter import Widget
from django import forms
from entrepot.models import Conteneur
from entrepot.models.LigneReception import LigneReception


from entrepot.models.Produit import Produit
from entrepot.models.Reception import Reception
from entrepot.models.Zone import Zone


class ExpeditionForm(forms.Form):
    nom=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control'}))
    date=forms.DateField(widget=forms.DateInput(attrs={'class':'form-control'}))
    ligneReception=forms.ModelMultipleChoiceField(queryset=LigneReception.objects.filter(expedier=False), widget = forms.SelectMultiple(attrs={'class':'form-control'}),label='Ligne réception')
    numCont=forms.ModelChoiceField(empty_label='choisir le conteneur',queryset=Conteneur.objects.all(),widget = forms.Select(attrs={'class':'form-control'}),label='Numéro conteneur')
    
    
        