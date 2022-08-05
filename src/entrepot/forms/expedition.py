
from  entrepot.models.Client import Client

from django import forms
from entrepot.models import Conteneur
from entrepot.models.LigneReception import LigneReception
from entrepot.models.Bateau import Bateau


class ExpeditionForm(forms.Form):
    nom=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control'}))
    date=forms.DateField(widget=forms.DateInput(attrs={'class':'form-control'}))
    ligneReception=forms.ModelMultipleChoiceField(queryset=LigneReception.objects.filter(expedier=False), widget = forms.SelectMultiple(attrs={'class':'form-control'}),label='Ligne réception')
    numCont=forms.ModelChoiceField(empty_label='choisir le conteneur',queryset=Conteneur.objects.all(),widget = forms.Select(attrs={'class':'form-control'}),label='Numéro conteneur')
    client=forms.ModelChoiceField(empty_label='choisir le client',queryset=Client.objects.all(),widget = forms.Select(attrs={'class':'form-control'}))
    bateau=forms.ModelChoiceField(empty_label='choisir le bateau',queryset=Bateau.objects.all(),widget = forms.Select(attrs={'class':'form-control'}))
        