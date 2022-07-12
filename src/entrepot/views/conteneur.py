from django.shortcuts import render
from entrepot.models.Conteneur import Conteneur
from django.core.paginator import Paginator,EmptyPage

def conteneur_list(request):
    selected="conteneur"
    conteneur_list=Conteneur.objects.all()
    
    paginator= Paginator(conteneur_list.order_by('-dateCreation'),10)
    
    try:
        page= request.GET.get(page)
        if not page:
            page=1
            conteneur_list=paginator.page(page)
    except EmptyPage:
        conteneur_list=paginator.page(paginator.num_pages())
    return render(request,"entrepot/conteneur/conteneur_list.html",locals())
         