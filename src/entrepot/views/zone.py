from django.shortcuts import render
from entrepot.models.Zone import Zone
from django.core.paginator import Paginator,EmptyPage

def zone_list(request):
    selected="zones"
    zone_list=Zone.objects.all()
    
    paginator= Paginator(zone_list.order_by('-dateCreation'),10)
    
    try:
        page= request.GET.get(page)
        if not page:
            page=1
            zone_list=paginator.page(page)
    except EmptyPage:
        zone_list=paginator.page(paginator.num_pages())
    return render(request,"entrepot/zone/zone_list.html",locals())
         