from django.contrib import admin
from entrepot.models.Categorie import Categorie
from entrepot.models.Fournisseur import Fournisseur

from entrepot.models.Reception import Reception

# Register your models here.
@admin.register(Reception)
class ReceptionAdmin(admin.ModelAdmin):
    pass

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    pass

@admin.register(Fournisseur)
class FournisseurAdmin(admin.ModelAdmin):
    pass


