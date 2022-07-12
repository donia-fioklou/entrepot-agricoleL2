from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from entrepot.models.Fournisseur import Fournisseur


# Register your models here.
@admin.register(Fournisseur)
class FournisseurAdmin(ImportExportModelAdmin):
    pass

