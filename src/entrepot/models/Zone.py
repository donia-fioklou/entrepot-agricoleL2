from django.db import models

from entrepot.models.Entrepot import Entrepot
from entrepot.models.Expedition import Expedition
from entrepot.models.Reception import Reception


class Zone(models.Model):
    entrepot=models.ForeignKey(Entrepot,on_delete=models.CASCADE)
    nom=models.CharField(max_length=50)
    qteMax=models.IntegerField()
    qteActu=models.IntegerField( blank=True, null=True)
    reception=models.ManyToManyField(Reception)
    expedition=models.ManyToManyField(Expedition)
    dateCreation=models.DateField( auto_now_add=True)
    
    def __str__(self):
        return  self.nom
    
    class Meta():
        verbose_name="Zone"