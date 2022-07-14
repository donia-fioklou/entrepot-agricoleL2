from unicodedata import name
from django.urls import path
from entrepot.views.categorie import CategorieDeleteView, CategorieDetail, UpdateCategorie, categorie_list_create
from entrepot.views.fournisseur import  FournisseurDeleteView, FournisseurDetail, UpdateFournisseur,  fournisseur_list_create
from entrepot.views.indexView import IndexView



from entrepot.views.login import login_user
from entrepot.views.produit import ProduitDeleteView, ProduitDetail, UpdateProduit, produit_list_create


urlpatterns = [
    path('',login_user,name="login"),
    #path('',IndexView.as_view(),name='home'),
    path('fournisseurs/', fournisseur_list_create,name="fournisseurs"),
    path('categories/', categorie_list_create,name="categories"),
    path('produits/', produit_list_create,name="produits"),
    
    path('fournisseurs/<int:pk>', FournisseurDetail.as_view(),name="detail_fournisseurs"),
    path('categories/<int:pk>', CategorieDetail.as_view(),name="detail_categories"),
    path('produits/<int:pk>', ProduitDetail.as_view(),name="detail_produits"),
    
    path('fournisseurs/delete/<int:pk>', FournisseurDeleteView.as_view(),name="delete_fournisseurs"),
    path('categories/delete/<int:pk>', CategorieDeleteView.as_view(),name="delete_categories"),
    path('produits/delete/<int:pk>', ProduitDeleteView.as_view(),name="delete_produits"),
    #path('fournisseurs/create/',CreateFournisseur.as_view(),name="create_fournisseurs"),
    path('fournisseurs/update/<int:pk>/',UpdateFournisseur.as_view(),name="update_fournisseurs"),
    path('categorie/update/<int:pk>/',UpdateCategorie.as_view(),name="update_categories"),
    path('produit/update/<int:pk>/',UpdateProduit.as_view(),name="update_produits"),
    
]