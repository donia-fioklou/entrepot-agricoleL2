from django.db import models

from entrepot.models.Bateau import Bateau
class Conteneur(models.Model):
    IdProprietaire=models.CharField(max_length=4,null=True)
    numCon=models.PositiveIntegerField(max_length=6,null=True)
    typeCon=models.CharField(max_length=4,null=True)
    dateCreation=models.DateField(auto_now=False, auto_now_add=True)
    bateau=models.ForeignKey(Bateau, on_delete=models.CASCADE,null=True)
    def __str__(self):
        
        
        return  self.IdProprietaire
    
    class Meta():
        verbose_name="Conteneur"