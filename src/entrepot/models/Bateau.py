from django.db import models
class Bateau(models.Model):
    nom=models.CharField(max_length=100)
    immatriculation=models.CharField(max_length=100)
    dateCreation=models.DateField(auto_now=False, auto_now_add=True)
    
    def __str__(self):
        return  self.nom
    
    class Meta():
        verbose_name="Bateau"