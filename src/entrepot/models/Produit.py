from django.db import models

from entrepot.models.Categorie import Categorie

class Produit(models.Model):
    nomProd=models.CharField(max_length=50)
    categorie=models.ForeignKey( Categorie, on_delete=models.CASCADE)
    dateCreation=models.DateField( auto_now_add=True)
    
    def __str__(self):
        return  self.nomProd
    
    class Meta():
        verbose_name="Produit"
        
    
    