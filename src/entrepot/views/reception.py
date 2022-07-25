
from ast import For, NotIn
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from entrepot.forms.addZone import AddZone
from entrepot.forms.produit import ProduitForm
from entrepot.models.Fournisseur import Fournisseur
from entrepot.models.LigneReception import LigneReception
from entrepot.models.Produit import Produit
from entrepot.models.Reception import Reception
from entrepot.forms.reception import ReceptionForm
from django.core.paginator import Paginator,EmptyPage

from entrepot.models.Zone import Zone

def reception_list_create(request):
    
    form= ReceptionForm(request.POST or None)
    if request.method=='POST' and form.is_valid():
        nom=request.POST.get('nom')
        date=request.POST.get('date')
        
        prod=request.POST.get('produit')
        produit=Produit.objects.get(id=prod)
        
        four=request.POST.get('fournisseur')
        fournisseur=Fournisseur.objects.get(id=four)
        
        qteProd=request.POST.get('qteProd')
        numLot=request.POST.get('numLot')
        
        reception=Reception.objects.create(nomRecep=nom,dateRecep=date,produit=produit,fournisseur=fournisseur)
        zo=request.POST.getlist('zone')
        for element in zo:
            zone=Zone.objects.get(id=element)
            ligneReception=LigneReception.objects.create(numLot=numLot,reception=reception,qteProd=qteProd,zone=zone,)
        form=ReceptionForm()
        
    listReception=Reception.objects.all()
    paginator= Paginator(listReception.order_by('-dateCreation'),10)
    try:
        page= request.GET.get("page")
        if not page:
            page=1
            listReception=paginator.page(page)
    except EmptyPage:
        listReception=paginator.page(paginator.num_pages())
 
    return render(request,"entrepot/reception/reception_list.html",locals())

def receptionUpdate(request,id):
    reception=Reception.objects.get(id=id)
    ligneReception=LigneReception.objects.filter(reception=id)
    formRecep=ReceptionForm(request.POST or None,isinstance=[Reception,LigneReception])
    

def ajouterZone(request,id):
    form=AddZone(request.POST or None)
    if request.method=='POST' and form.is_valid():
        
        ligneReception=LigneReception.objects.filter(reception=id)
        numLot=ligneReception.values()[0]["numLot"]
        reception =Reception.objects.get(id=id)
        qteProd=ligneReception.values()[0]['qteProd']
        
        listZone=Zone.objects.exclude(lignereception__reception=id)   
        zo=request.POST.getlist('zone')
        for element in zo:
            zone=Zone.objects.get(id=element)
            if zone  in listZone:
                ligneReception=LigneReception.objects.create(numLot=numLot,reception=reception,qteProd=qteProd,zone=zone,)
                
        return HttpResponseRedirect(reverse("receptions"))
    return render(request,"entrepot/reception/ajouter_zone.html",locals())

def receptionDelete(request,id):
        if request.method =="POST":
            ligneReception=LigneReception.objects.filter(reception=id)
            for element in ligneReception:
                element.delete()
            reception=Reception.objects.get(id=id).delete()
            return HttpResponseRedirect(reverse("receptions"))
        return render(request,"entrepot/reception/reception_confirm_delete.html",locals())

def receptionDetail(request,id):
    reception=Reception.objects.get(id=id)
    zone=Zone.objects.filter(lignereception__reception=id)
    listZone=[]
    for element in zone:
        listZone.append(element.nom)
    chainZone=",".join(listZone)
    return render(request,"entrepot/reception/reception_detail.html",locals())




