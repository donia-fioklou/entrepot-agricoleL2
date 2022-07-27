
from tkinter import Widget
from django import forms

from entrepot.models.Fournisseur import Fournisseur
from entrepot.models.Produit import Produit
from entrepot.models.Zone import Zone


class ReceptionForm(forms.Form):
    nom=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control'}))
    date=forms.DateField(widget=forms.DateInput(attrs={'class':'form-control'}))
    fournisseur=forms.ModelChoiceField( empty_label='choisir le fournisseur', queryset=Fournisseur.objects.all(),widget = forms.Select(attrs={'class':'form-control'}))
    produit=forms.ModelChoiceField(empty_label='choisir le produit',queryset=Produit.objects.all(), widget = forms.Select(attrs={'class':'form-control'}))
    qteProd=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}),label='Quantité')
    numLot=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control'}))
    zone=forms.ModelMultipleChoiceField(queryset=Zone.objects.all(), widget = forms.SelectMultiple(attrs={'class':'form-control'}))
    

            