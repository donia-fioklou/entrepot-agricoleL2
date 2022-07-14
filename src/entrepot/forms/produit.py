from django import forms
from django.forms import ModelForm


from entrepot.models.Produit import Produit


class ProduitForm (ModelForm):
    class Meta:
        model=Produit
        fields=("nomProd","categorie")
        labels={
            "nomProd":"Produit",
            "categorie":"catégorie"
        }
        widgets={
            'nomProd': forms.TextInput(attrs={'class':'form-control'}),
            'categorie':forms.Select(attrs={'class':'form-control'})
        }
    