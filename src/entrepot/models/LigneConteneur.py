from django.db import models
from entrepot.models.Conteneur import Conteneur
from entrepot.models.Expedition import Expedition
from entrepot.models.LigneReception import LigneReception




class LigneConteneur(models.Model):
    ligneReception=models.ForeignKey(LigneReception, on_delete=models.CASCADE)
    conteneur=models.ForeignKey(Conteneur, on_delete=models.CASCADE)
    expedition=models.ForeignKey(Expedition,on_delete=models.CASCADE)
    