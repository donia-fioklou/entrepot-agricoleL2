from django.shortcuts import render
from entrepot.models.LigneReception import LigneReception
from django.core.paginator import Paginator,EmptyPage

def ligneReception_list(request):
    selected="ligneReception"
    ligneReception_list=LigneReception.objects.all()
    
    paginator= Paginator(ligneReception_list.order_by('-dateCreation'),10)
    
    try:
        page= request.GET.get(page)
        if not page:
            page=1
            ligneReception_list=paginator.page(page)
    except EmptyPage:
        ligneReception_list=paginator.page(paginator.num_pages())
    return render(request,"entrepot/ligneReception/ligneReception_list.html",locals())
         