from django.db import models

from entrepot.models.Categorie import Categorie
from entrepot.models.Fournisseur import Fournisseur

class Reception(models.Model):
    fournisseur=models.ForeignKey(Fournisseur,on_delete=models.CASCADE)
    nomRecep=models.CharField(max_length=30)
    dateRecep=models.DateField()
    dateCreation=models.DateField(auto_now_add=True)

    
    def __str__(self):
        return self.nomProd
    
    
    
    