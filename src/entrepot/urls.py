from unicodedata import name
from django.urls import path
from entrepot.views.fournisseur import CreateFournisseur, FournisseurDeleteView, FournisseurDetail, UpdateFournisseur, fournisseur_list,DetailView
from entrepot.views.indexView import IndexView

from entrepot.views.login import login_user


urlpatterns = [
    path('login_user/',login_user,name="login"),
    path('',IndexView.as_view(),name='home'),
    path('fournisseurs/', fournisseur_list,name="fournisseurs"),
    path('fournisseurs/<int:pk>', FournisseurDetail.as_view(),name="detail_fournisseurs"),
    path('fournisseurs/delete/<int:pk>', FournisseurDeleteView.as_view(),name="delete_fournisseurs"),
    path('fournisseurs/create/',CreateFournisseur.as_view(),name="create_fournisseurs"),
    path('fournisseurs/update/<int:pk>/',UpdateFournisseur.as_view(),name="update_fournisseurs"),
    
]