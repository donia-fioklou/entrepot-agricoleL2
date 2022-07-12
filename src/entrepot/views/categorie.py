from django.shortcuts import render
from entrepot.models.Categorie import Categorie
from django.core.paginator import Paginator,EmptyPage

def categorie_list(request):
    selected="categories"
    categorie_list=Categorie.objects.all()
    
    paginator= Paginator(categorie_list.order_by('-dateCreation'),10)
    
    try:
        page= request.GET.get(page)
        if not page:
            page=1
            categorie_list=paginator.page(page)
    except EmptyPage:
        categorie_list=paginator.page(paginator.num_pages())
    return render(request,"entrepot/categorie/categorie_list.html",locals())
         