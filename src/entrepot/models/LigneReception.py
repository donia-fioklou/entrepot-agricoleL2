from django.db import models
from entrepot.models.Expedition import Expedition
from entrepot.models.Reception import Reception
from entrepot.models.Zone import Zone
class LigneReception(models.Model):
    reception=models.ForeignKey(Reception, on_delete=models.CASCADE)
    zone=models.ForeignKey(Zone, on_delete=models.CASCADE)
    qteProd=models.PositiveIntegerField()
    numLot=models.CharField(max_length=100) 
    dateCreation=models.DateField( auto_now_add=True)
    expedier=models.BooleanField(default=False)
    
    
    def __str__(self):
        champs=" reception: {}| zone: {} ".format(self.reception,self.zone)
        return champs