
from django.shortcuts import render

from entrepot.forms.expedition import ExpeditionForm
from entrepot.models import Expedition, Zone
from entrepot.models.Conteneur import Conteneur
from entrepot.models.LigneReception import LigneReception
from entrepot.models.LigneConteneur import LigneConteneur
from django.core.paginator import Paginator,EmptyPage


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
        
        for i in ligneReception:
            ligneReception=LigneReception.objects.get(id=i)
            ligneReception.expedier=True
            ligneReception.save()
            ligneConteneur=LigneConteneur.objects.create(ligneReception=ligneReception,conteneur=conteneur)
        
        expedition=Expedition.objects.create(conteneur=conteneur,nomExp=nom,dateExp=date)

            
    listExpedition=Expedition.objects.all()
    
    paginator= Paginator(listExpedition.order_by('-dateCreation'),10)
    try:
        page= request.GET.get("page")
        if not page:
            page=1
            listExpedition=paginator.page(page)
    except EmptyPage:
        listExpedition=paginator.page(paginator.num_pages())
        
        
    return  render(request,"entrepot/expedition/expedition_list.html",locals())


def expeditionDetail(request,id):
    expedition=Expedition.objects.get(id=id)
    zone=Zone.objects.filter(ligneReception_expedier=True).filter(ligneConteneur_conn)
    listZone=[]
    for element in zone:
        listZone.append(element.nom)
    chainZone=",".join(listZone)
    return render(request,"entrepot/expedition/expedition_detail.html",locals())