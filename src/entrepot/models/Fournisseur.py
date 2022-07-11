from django.db import models 


class Fournisseur(models.Model):
    nom=models.CharField(max_length=50)
    contact=models.IntegerField()
    email=models.EmailField( max_length=200)
    adresse=models.CharField(max_length=200)