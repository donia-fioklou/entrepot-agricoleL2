from django.db import models

from entrepot.models.Categorie import Categorie
from entrepot.models.Reception import Reception
class Produit(models.Model):
    nomProd=models.CharField(max_length=50)
    categorie=models.ForeignKey( Categorie, on_delete=models.CASCADE)
    reception=models.ManyToManyField(Reception)
    
    