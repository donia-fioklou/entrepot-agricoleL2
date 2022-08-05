from entrepot.models.Client import Client
from django.db import models
from entrepot.models.Conteneur import Conteneur




class Expedition(models.Model):
    conteneur=models.ForeignKey(Conteneur, on_delete=models.CASCADE)
    client=models.ForeignKey(Client, on_delete=models.CASCADE,null=True)
    nomExp=models.CharField(max_length=50,blank=True,unique=True)
    dateExp=models.DateField()
    qte=models.IntegerField(blank=True,null=True)
    dateCreation=models.DateField( auto_now_add=True)
    
    def __str__(self):
        return self.nomExp
