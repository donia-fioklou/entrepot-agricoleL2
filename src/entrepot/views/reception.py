
from ast import For, NotIn
from urllib import request
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from entrepot.decorators import allowed_users
from entrepot.forms.addZone import AddZone
from entrepot.forms.editReception import LigneRecepForm, RecepForm
from entrepot.forms.produit import ProduitForm
from entrepot.models.Fournisseur import Fournisseur
from entrepot.models.LigneReception import LigneReception
from entrepot.models.Produit import Produit
from entrepot.models.Reception import Reception
from entrepot.forms.reception import ReceptionForm
from django.core.paginator import Paginator,EmptyPage
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from entrepot.models.Zone import Zone



def is_valid_queryparam(param):
    return param != '' and param is not None

@login_required
@allowed_users(allowed_roles=['quai','admin'])
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
        messages.success(request,"Enregistrer avec success") 
    else:   
        messages.error(request,"Désolé, vous n'avez pas réussie l'enregistrement, réessayer")
          
    listReception=Reception.objects.all()
    nomRecep=request.GET.get('nomRecep')
    
    if is_valid_queryparam(nomRecep):
        listReception=listReception.filter(nomRecep=nomRecep)
        
    
    paginator= Paginator(listReception.order_by('-dateCreation'),10)
    try:
        page= request.GET.get("page")
        if not page:
            page=1
            listReception=paginator.page(page)
    except EmptyPage:
        listReception=paginator.page(paginator.num_pages())
 
    return render(request,"entrepot/reception/reception_list.html",locals())

@login_required
@allowed_users(allowed_roles=['quai'])
def receptionUpdate(request,id):
    reception=Reception.objects.get(id=id)
    ligneReception=LigneReception.objects.filter(reception=id)
    a=ligneReception.first()
    form1=RecepForm(request.POST or None,instance=reception)
    form2=LigneRecepForm(request.POST or None,instance=a)
    if request.method=='POST' and form1.is_valid() and form2.is_valid():
        form1.save()
        qteProd=request.POST.get('qteProd')
        numLot=request.POST.get('numLot')
        for i in ligneReception:
            i.qteProd=qteProd
            i.save()
            i.numLot=numLot
            i.save()
        return HttpResponseRedirect(reverse("receptions"))       
    
    
    return render(request,"entrepot/reception/reception_form.html",locals())
    

    
@login_required
@allowed_users(allowed_roles=['quai'])
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

@login_required
@allowed_users(allowed_roles=['quai','admin'])
def retirerZone(request,id):
    form=AddZone(request.POST or None)
    if request.method=="POST" and form.is_valid():
        zo=request.POST.getlist('zone')
        
        ligneReception=LigneReception.objects.filter(reception=id)
        for i in ligneReception:
            if i.zone == zo:
                i.delete()
        return HttpResponseRedirect(reverse("receptions"))
    return render(request,"entrepot/reception/retirer_zone.html",locals())
    
@login_required
@allowed_users(allowed_roles=['quai','admin'])
def receptionDelete(request,id):
        if request.method =="POST":
            ligneReception=LigneReception.objects.filter(reception=id)
            for element in ligneReception:
                element.delete()
            reception=Reception.objects.get(id=id).delete()
            return HttpResponseRedirect(reverse("receptions"))
        return render(request,"entrepot/reception/reception_confirm_delete.html",locals())

@login_required
@allowed_users(allowed_roles=['quai','admin'])

def receptionDetail(request,id):
    reception=Reception.objects.get(id=id)
    zone=Zone.objects.filter(lignereception__reception=id)
    listZone=[]
    for element in zone:
        listZone.append(element.nom)
    chainZone=",".join(listZone)
    return render(request,"entrepot/reception/reception_detail.html",locals())





