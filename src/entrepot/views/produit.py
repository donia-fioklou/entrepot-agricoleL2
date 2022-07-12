from django.shortcuts import render
from entrepot.models.Produit import Produit
from django.core.paginator import Paginator,EmptyPage

def produit_list(request):
    selected="produits"
    produit_list=Produit.objects.all()
    
    paginator= Paginator(produit_list.order_by('-dateCreation'),10)
    
    try:
        page= request.GET.get(page)
        if not page:
            page=1
            produit_list=paginator.page(page)
    except EmptyPage:
        produit_list=paginator.page(paginator.num_pages())
    return render(request,"entrepot/produit/produit_list.html",locals())
         