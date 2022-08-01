from django.db import models
from entrepot.models.Entrepot import Entrepot



class Zone(models.Model):
    entrepot=models.ForeignKey(Entrepot,on_delete=models.CASCADE)
    nom=models.CharField(max_length=50)
    qteMax=models.PositiveIntegerField()
    qteActu=models.PositiveIntegerField( blank=True, null=True)
    dateCreation=models.DateField( auto_now_add=True)
    
    def __str__(self):
        return  self.nom
    
    class Meta():
        verbose_name="Zone"