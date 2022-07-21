from unicodedata import name
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from entrepot.decorators import allowed_users
from entrepot.forms.entrepot import EntrepotForm
from entrepot.models.Entrepot import Entrepot
from django.core.paginator import Paginator,EmptyPage
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import DetailView,ListView
from django.contrib.auth.decorators import login_required
from projetStage.settings import LOGIN_REDIRECT_URL
from django.contrib.auth.mixins import LoginRequiredMixin
def is_valid_queryparam(param):
    return param != '' and param is not None
@login_required
@allowed_users(allowed_roles=['admin'])
def entrepot_list_create(request):
    
    form= EntrepotForm(request.POST or None)
    if request.method=='POST' and form.is_valid():
        form.save()
        form=EntrepotForm()

    
    entrepot_list=Entrepot.objects.all()
    nom=request.GET.get('nom')
    adresse=request.GET.get('adresse')
    
    if is_valid_queryparam(nom):
        entrepot_list=entrepot_list.filter(nom=nom)
    elif is_valid_queryparam(adresse):
        entrepot_list=entrepot_list.filter(adresse=adresse)
        
    
    
    
    paginator= Paginator(entrepot_list.order_by('-dateCreation'),10)
    
    try:
        page= request.GET.get("page")
        if not page:
            page=1
            entrepot_list=paginator.page(page)
    except EmptyPage:
        entrepot_list=paginator.page(paginator.num_pages())
    return render(request,"entrepot/entrepot/entrepot_list.html",locals())




"""
class CreateEntrepot(CreateView):
    model=Entrepot
    form_class=EntrepotForm
    template_name="entrepot/entrepot/entrepot_form.html"
    
    def get_success_url(self):
        return reverse_lazy("detail_entrepots",kwargs={"pk":self.object.pk})
"""

class UpdateEntrepot(LoginRequiredMixin,UpdateView):
    model=Entrepot
    form_class=EntrepotForm
    template_name="entrepot/entrepot/entrepot_form.html"
    
    def get_success_url(self):
        return reverse_lazy("detail_entrepots",kwargs={"pk":self.object.pk})
    
class EntrepotDeleteView(LoginRequiredMixin,DeleteView):
    model = Entrepot
    template_name="entrepot/entrepot/entrepot_confirm_delete.html"
    
    def get_success_url(self):
        return reverse_lazy("entrepots")


class EntrepotDetail(LoginRequiredMixin,DetailView):
    model = Entrepot
    template_name = "entrepot/entrepot/entrepot_detail.html"
    

         