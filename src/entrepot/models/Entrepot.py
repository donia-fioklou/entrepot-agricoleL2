from django.db import models
class Entrepot(models.Model):
    nom=models.CharField(max_length=50)
    adresse=models.CharField(max_length=50)