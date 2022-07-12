from django.shortcuts import render
from entrepot.models.Reception import Reception
from django.core.paginator import Paginator,EmptyPage

def reception_list(request):
    selected="receptions"
    reception_list=Reception.objects.all()
    
    paginator= Paginator(reception_list.order_by('-dateRecep'),10)
    
    try:
        page= request.GET.get(page)
        if not page:
            page=1
            reception_list=paginator.page(page)
    except EmptyPage:
        reception_list=paginator.page(paginator.num_pages())
    return render(request,"entrepot/reception/reception_list.html",locals())
         