from django.db import models

from entrepot.models.Entrepot import Entrepot
from entrepot.models.Expedition import Expedition
from entrepot.models.Reception import Reception


class Zone(models.Model):
    entrepot=models.ForeignKey(Entrepot,on_delete=models.CASCADE)
    nom=models.CharField(max_length=50)
    reception=models.ManyToManyField(Reception)
    expedition=models.ManyToManyField(Expedition)