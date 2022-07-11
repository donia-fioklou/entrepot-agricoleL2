from django.db import models

from entrepot.models.Conteneur import Conteneur



class Expedition(models.Model):
    conteneur=models.ForeignKey(Conteneur, on_delete=models.CASCADE)
    nomExp=models.CharField(max_length=50)
    dateExp=models.DateField()
    qte=models.IntegerField
    poids=models.FloatField
