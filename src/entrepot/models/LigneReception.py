from django.db import models
from entrepot.models.Expedition import Expedition

from entrepot.models.Reception import Reception
from entrepot.models.Zone import Zone
class LigneReception(models.Model):
    reception=models.ForeignKey(Reception, on_delete=models.CASCADE)
    expedition=models.ForeignKey(Expedition, on_delete=models.CASCADE)
    
    qteProd=models.IntegerField
    poids=models.FloatField
    numLot=models.CharField(max_length=100) 