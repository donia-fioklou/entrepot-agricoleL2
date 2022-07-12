from django.shortcuts import render
from entrepot.models.Entrepot import Entrepot
from django.core.paginator import Paginator,EmptyPage

def entrepot_list(request):
    selected="entrepots"
    entrepot_list=Entrepot.objects.all()
    
    paginator= Paginator(entrepot_list.order_by('-dateCreation'),10)
    
    try:
        page= request.GET.get(page)
        if not page:
            page=1
            entrepot_list=paginator.page(page)
    except EmptyPage:
        entrepot_list=paginator.page(paginator.num_pages())
    return render(request,"entrepot/entrepot/entrepot_list.html",locals())
         