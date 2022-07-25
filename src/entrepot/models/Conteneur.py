from django.db import models
class Conteneur(models.Model):
    numCon=models.CharField(max_length=100)
    dateCreation=models.DateField(auto_now=False, auto_now_add=True)
    
    def __str__(self):
        return  self.numCon
    
    class Meta():
        verbose_name="Conteneur"