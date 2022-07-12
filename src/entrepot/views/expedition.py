from django.shortcuts import render
from entrepot.models.Expedition import Expedition
from django.core.paginator import Paginator,EmptyPage

def expedition_list(request):
    selected="expédition"
    expedition_list=Expedition.objects.all()
    
    paginator= Paginator(expedition_list.order_by('-dateCreation'),10)
    
    try:
        page= request.GET.get(page)
        if not page:
            page=1
            expedition_list=paginator.page(page)
    except EmptyPage:
        expedition_list=paginator.page(paginator.num_pages())
    return render(request,"entrepot/expedition/expedition_list.html",locals())
         