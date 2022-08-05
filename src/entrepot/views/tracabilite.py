from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from entrepot.decorators import allowed_users
from django.core.paginator import Paginator,EmptyPage
from django.contrib.auth.decorators import login_required
from entrepot.models.Conteneur import Conteneur

from entrepot.models.Expedition import Expedition
from entrepot.models.LigneConteneur import LigneConteneur
from entrepot.models.LigneReception import LigneReception

def is_valid_queryparam(param):
    return param != '' and param is not None
@login_required
@allowed_users(allowed_roles=['quai','admin'])
def tracabilite_list(request):
        listeExpedition=Expedition.objects.all()
        
                
        listExpedition=Expedition.objects.all()
        nomExp=request.GET.get('nomExp')
        
        if is_valid_queryparam(nomExp):
            listExpedition=listExpedition.filter(nomExp=nomExp)
        
        paginator= Paginator(listExpedition.order_by('-dateCreation'),10)
        try:
            page= request.GET.get("page")
            if not page:
                page=1
                listExpedition=paginator.page(page)
        except EmptyPage:
            listExpedition=paginator.page(paginator.num_pages())
        
        return  render(request,"entrepot/tracabilite/tracabilite_list.html",locals())

def tracabiliteDetail(request,id):
    expedition=Expedition.objects.get(id=id)
    expeditionList=Expedition.objects.filter(id=id)
    expeditionId=expeditionList.values()[0]["id"]
    leConteneur=Conteneur.objects.get(expedition__id=expeditionId)
    ligneConteneur=LigneConteneur.objects.filter(expedition=expedition.id)
    iId=[]
    for i in ligneConteneur:
       iId.append(LigneReception.objects.get(id=i.ligneReception_id))
    

    return render(request,"entrepot/tracabilite/tracabilite_detail.html",locals())