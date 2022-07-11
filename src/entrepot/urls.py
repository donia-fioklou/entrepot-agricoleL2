from unicodedata import name
from django.urls import path
from entrepot.views.indexView import IndexView

from entrepot.views.login import login_user


urlpatterns = [
    path('login_user',login_user,name="login"),
    path('',IndexView.as_view(),name='home')
    
    
]