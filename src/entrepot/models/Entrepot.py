from django.db import models
class Entrepot(models.Model):
    nom=models.CharField(max_length=50)
    adresse=models.CharField(max_length=50)
    dateCreation=models.DateField(auto_now=False, auto_now_add=True)
    
        
    def __str__(self):
        return  self.nom
    
    class Meta():
        verbose_name="Entrepot"