from django import forms

from entrepot.models.Produit import Produit


class DashbordProd(forms.Form):
    produit=forms.ModelChoiceField(empty_label='choisir le produit',queryset=Produit.objects.all(), widget = forms.Select(attrs={'class':'form-control'}))