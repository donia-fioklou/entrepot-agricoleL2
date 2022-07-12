from django.db import models
class Categorie(models.Model):
    nom=models.CharField(max_length=50)
    dateCreation=models.DateField( auto_now_add=True,null=False)
