import json
from multiprocessing import context
from re import T
from django.shortcuts import render
from entrepot.decorators import allowed_users
from django.contrib.auth.decorators import login_required
from entrepot.forms.dashbordProd import DashbordProd
from entrepot.models.LigneReception import LigneReception
from django.db.models import Sum
from entrepot.models.Reception import Reception

@login_required
@allowed_users(allowed_roles=['admin','quai'])
def dashbord(request):
    form=DashbordProd(request.POST or None)

    prod=request.GET.get('produit')
            
    
    quantiteRecep=[]
    for i in range(1,13):
        ligneReception=LigneReception.objects.filter(reception__produit=prod).filter(reception__dateRecep__month=i)
        a=ligneReception.aggregate(qteSum=Sum('qteProd'))
        quantiteRecep.append(a)
    listRecep=[]
    for i in quantiteRecep:
        listRecep.append(i["qteSum"])
        
    data1=json.dumps(listRecep)
    
    quantiteExp=[]
    for i in range(1,13):
        ligneExpedition=LigneReception.objects.filter(reception__produit=prod).filter(reception__dateRecep__month=i).filter(expedier=True)
        a=ligneExpedition.aggregate(qteSum=Sum('qteProd'))
        quantiteExp.append(a)
    listExp=[]
    for i in quantiteExp:
        listExp.append(i["qteSum"])
    data2=json.dumps(listExp)
    return render(request,'entrepot/widgets/charts.html',locals())