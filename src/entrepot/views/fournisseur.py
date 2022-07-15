from unicodedata import name
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from entrepot.forms.fournisseur import FournisseurForm
from entrepot.models.Fournisseur import Fournisseur
from django.core.paginator import Paginator,EmptyPage
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import DetailView,ListView

def is_valid_queryparam(param):
    return param != '' and param is not None

def fournisseur_list_create(request):
    
    form= FournisseurForm(request.POST or None)
    if request.method=='POST' and form.is_valid():
        form.save()

    selected="fournisseurs"
    fournisseur_list=Fournisseur.objects.all()
    nom=request.GET.get('nom')
    adresse=request.GET.get('adresse')
    
    if is_valid_queryparam(nom):
        fournisseur_list=fournisseur_list.filter(nom=nom)
    elif is_valid_queryparam(adresse):
        fournisseur_list=fournisseur_list.filter(adresse=adresse)
        
    
    
    
    paginator= Paginator(fournisseur_list.order_by('-dateCreation'),10)
    
    try:
        page= request.GET.get("page")
        if not page:
            page=1
            fournisseur_list=paginator.page(page)
    except EmptyPage:
        fournisseur_list=paginator.page(paginator.num_pages())
    return render(request,"entrepot/fournisseur/fournisseur_list.html",locals())




"""
class CreateFournisseur(CreateView):
    model=Fournisseur
    form_class=FournisseurForm
    template_name="entrepot/fournisseur/fournisseur_form.html"
    
    def get_success_url(self):
        return reverse_lazy("detail_fournisseurs",kwargs={"pk":self.object.pk})
"""

class UpdateFournisseur(UpdateView):
    model=Fournisseur
    form_class=FournisseurForm
    template_name="entrepot/fournisseur/fournisseur_form.html"
    
    def get_success_url(self):
        return reverse_lazy("detail_fournisseurs",kwargs={"pk":self.object.pk})
    
class FournisseurDeleteView(DeleteView):
    model = Fournisseur
    template_name="entrepot/fournisseur/fournisseur_confirm_delete.html"
    
    def get_success_url(self):
        return reverse_lazy("fournisseurs")


class FournisseurDetail(DetailView):
    model = Fournisseur
    template_name = "entrepot/fournisseur/fournisseur_detail.html"
    

         