
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from entrepot.forms.expedition import ExpeditionForm
from entrepot.models import Expedition, Zone
from entrepot.models.Conteneur import Conteneur
from entrepot.models.LigneReception import LigneReception
from entrepot.models.LigneConteneur import LigneConteneur
from django.core.paginator import Paginator,EmptyPage

from entrepot.views import conteneur

def is_valid_queryparam(param):
    return param != '' and param is not None
def expedition_list_create(request):
    form= ExpeditionForm(request.POST or None)
    if request.method=='POST' and form.is_valid():
        #expeLast=Expedition.objects.last()
        #nom='E0{}'.format(expeLast.values()['id']+1)
        nom=request.POST.get('nom')
        date=request.POST.get('date')
        numCon=request.POST.get('numCont')
        ligneReception=request.POST.getlist('ligneReception')
        conteneur=Conteneur.objects.get(id=numCon)
        expedition=Expedition.objects.create(conteneur=conteneur,nomExp=nom,dateExp=date)
        exp=Expedition.objects.last()
        for i in ligneReception:
            ligneReception=LigneReception.objects.get(id=i)
            ligneReception.expedier=True
            ligneReception.save()
            ligneConteneur=LigneConteneur.objects.create(ligneReception=ligneReception,conteneur=conteneur,expedition=exp)
            
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
        
        
    return  render(request,"entrepot/expedition/expedition_list.html",locals())

def expeditionUpdate(request,id):
    pass
    


def expeditionDetail(request,id):
    expedition=Expedition.objects.get(id=id)
    expeditionList=Expedition.objects.filter(id=id)
    expeditionId=expeditionList.values()[0]["id"]
    leConteneur=Conteneur.objects.get(expedition__id=expeditionId)
    ligneConteneur=LigneConteneur.objects.filter(expedition=expedition.id)
    iId=[]
    for i in ligneConteneur:
       iId.append(LigneReception.objects.get(id=i.ligneReception_id))
    

    return render(request,"entrepot/expedition/expedition_detail.html",locals())

def expeditionDelete(request,id):
    if request.method =="POST":
        expedition=Expedition.objects.get(id=id)
        ligneConteneur=LigneConteneur.objects.filter(conteneur__expedition__id=id)
        for i in ligneConteneur:
            i.delete()
        expedition.delete()
        return HttpResponseRedirect(reverse("expeditions"))
    return render(request,"entrepot/expedition/expedition_confirm_delete.html",locals())