from unicodedata import name
from django.urls import include, path
from entrepot.views.admin import admin
from entrepot.views.categorie import CategorieDeleteView, CategorieDetail, UpdateCategorie, categorie_list_create
from entrepot.views.conteneur import ConteneurDeleteView, ConteneurDetail, UpdateConteneur, conteneur_list_create
from entrepot.views.dashboard import dashbord
from entrepot.views.entrepot import EntrepotDeleteView, EntrepotDetail, UpdateEntrepot, entrepot_list_create
from entrepot.views.expedition import expedition_list_create, expeditionDelete, expeditionDetail
from entrepot.views.fournisseur import  FournisseurDeleteView, FournisseurDetail, UpdateFournisseur,  fournisseur_list_create
from entrepot.views.indexView import IndexView



from entrepot.views.login import login_user
from entrepot.views.produit import ProduitDeleteView, ProduitDetail, UpdateProduit, produit_list_create
from entrepot.views.reception import ajouterZone,reception_list_create, receptionDelete, receptionDetail, receptionUpdate, retirerZone
from entrepot.views.zone import UpdateZone, ZoneDeleteView, ZoneDetail, zone_list_create


urlpatterns = [
    path('admin/', admin ,name="admin"),
    path('',login_user,name="login"),
    path('dashboard',dashbord,name="dashboard"),
    
    #path('',IndexView.as_view(),name='home'),
    path('fournisseurs/', fournisseur_list_create,name="fournisseurs"),
    path('categories/', categorie_list_create,name="categories"),
    path('produits/', produit_list_create,name="produits"),
    path('entrepots/', entrepot_list_create,name="entrepots"),
    path('zones/', zone_list_create,name="zones"),
    path('receptions/', reception_list_create,name="receptions"),
    path('conteneurs/', conteneur_list_create,name="conteneurs"),
    path('receptions/ajouterZone/<int:id>', ajouterZone,name="ajouterZone"),
    path('receptions/retirerZone/<int:id>', retirerZone,name="retirerZone"),
    path('expeditions/', expedition_list_create,name="expeditions"),
    
    path('fournisseurs/<int:pk>', FournisseurDetail.as_view(),name="detail_fournisseurs"),
    path('categories/<int:pk>', CategorieDetail.as_view(),name="detail_categories"),
    path('produits/<int:pk>', ProduitDetail.as_view(),name="detail_produits"),
    path('entrepots/<int:pk>', EntrepotDetail.as_view(),name="detail_entrepots"),
    path('zones/<int:pk>', ZoneDetail.as_view(),name="detail_zones"),
    path('conteneurs/<int:pk>', ConteneurDetail.as_view(),name="detail_conteneurs"),
    path('receptions/<int:id>', receptionDetail,name="detail_receptions"),
    path('expedition/<int:id>', expeditionDetail,name="detail_expedition"),
    
    
    path('fournisseurs/delete/<int:pk>', FournisseurDeleteView.as_view(),name="delete_fournisseurs"),
    path('categories/delete/<int:pk>', CategorieDeleteView.as_view(),name="delete_categories"),
    path('produits/delete/<int:pk>', ProduitDeleteView.as_view(),name="delete_produits"),
    path('entrepot/delete/<int:pk>', EntrepotDeleteView.as_view(),name="delete_entrepots"),
    path('zones/delete/<int:pk>', ZoneDeleteView.as_view(),name="delete_zones"),
    path('conteneurs/delete/<int:pk>',ConteneurDeleteView.as_view() ,name="delete_conteneurs"),
    path('receptions/delete/<int:id>',receptionDelete ,name="delete_receptions"),
    path('expedition/delete/<int:id>',expeditionDelete ,name="delete_expedition"),
    
    
    path('fournisseurs/update/<int:pk>/',UpdateFournisseur.as_view(),name="update_fournisseurs"),
    path('categorie/update/<int:pk>/',UpdateCategorie.as_view(),name="update_categories"),
    path('produit/update/<int:pk>/',UpdateProduit.as_view(),name="update_produits"),
    path('entrepot/update/<int:pk>/',UpdateEntrepot.as_view(),name="update_entrepots"),
    path('zone/update/<int:pk>/',UpdateZone.as_view(),name="update_zones"),
    path('conteneur/update/<int:pk>/',UpdateConteneur.as_view(),name="update_conteneurs"),
    path('reception/update/<int:id>/',receptionUpdate,name="update_reception"),
]