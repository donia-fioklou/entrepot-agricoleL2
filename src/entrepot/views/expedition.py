

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from entrepot.decorators import allowed_users

from entrepot.forms.expedition import ExpeditionForm
from entrepot.models import Expedition, Zone
from entrepot.models.Bateau import Bateau
from entrepot.models.Client import Client
from entrepot.models.Conteneur import Conteneur
from entrepot.models.LigneReception import LigneReception
from entrepot.models.LigneConteneur import LigneConteneur
from django.core.paginator import Paginator,EmptyPage
from django.contrib.auth.decorators import login_required
from entrepot.views import conteneur
from django.contrib import messages

def is_valid_queryparam(param):
    return param != '' and param is not None
@login_required
@allowed_users(allowed_roles=['quai','admin'])
def expedition_list_create(request):
    form= ExpeditionForm(request.POST or None)
    if request.method=='POST' :
        if form.is_valid():
            #expeLast=Expedition.objects.last()
            #nom='E0{}'.format(expeLast.values()['id']+1)
            nom=request.POST.get('nom')
            date=request.POST.get('date')
            numCon=request.POST.get('numCont')
            cli=request.POST.get('client')
            ligneReception=request.POST.getlist('ligneReception')
            conteneur=Conteneur.objects.get(id=numCon)
            client=Client.objects.get(id=cli)
            expedition=Expedition.objects.create(conteneur=conteneur,nomExp=nom,dateExp=date,client=client)
            exp=Expedition.objects.last()
            for i in ligneReception:
                ligneReception=LigneReception.objects.get(id=i)
                ligneReception.expedier=True
                ligneReception.save()
                ligneConteneur=LigneConteneur.objects.create(ligneReception=ligneReception,conteneur=conteneur,expedition=exp)
            messages.success(request,"Enregistrer avec success") 
        else:
            messages.error(request,"Désolé, vous n'avez pas réussie l'enregistrement, réessayer")   
            
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
    #idConteneur=leConteneur.values()[0]["id"]
    #leBateau=Bateau.objects.get(conteneur__id=idConteneur)
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