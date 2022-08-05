from unicodedata import name
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from entrepot.decorators import allowed_users
from entrepot.forms.client import ClientForm
from entrepot.models.Client import Client
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
def client_list_create(request):
    
    form= ClientForm(request.POST or None)
    if request.method=='POST' and form.is_valid():
        form.save()
        form=ClientForm()

    selected="clients"
    client_list=Client.objects.all()
    nom=request.GET.get('nom')
    adresse=request.GET.get('adresse')
    
    if is_valid_queryparam(nom):
        client_list=client_list.filter(nom=nom)
    elif is_valid_queryparam(adresse):
        client_list=client_list.filter(adresse=adresse)
        
    
    
    
    paginator= Paginator(client_list.order_by('-dateCreation'),10)
    
    try:
        page= request.GET.get("page")
        if not page:
            page=1
            client_list=paginator.page(page)
    except EmptyPage:
        client_list=paginator.page(paginator.num_pages())
    return render(request,"entrepot/client/client_list.html",locals())




"""
class CreateClient(CreateView):
    model=Client
    form_class=ClientForm
    template_name="entrepot/client/client_form.html"
    
    def get_success_url(self):
        return reverse_lazy("detail_clients",kwargs={"pk":self.object.pk})
"""

class UpdateClient(LoginRequiredMixin,UpdateView):
    model=Client
    form_class=ClientForm
    template_name="entrepot/client/client_form.html"
    
    def get_success_url(self):
        return reverse_lazy("detail_clients",kwargs={"pk":self.object.pk})
    
class ClientDeleteView(LoginRequiredMixin,DeleteView):
    model = Client
    template_name="entrepot/client/client_confirm_delete.html"
    
    def get_success_url(self):
        return reverse_lazy("clients")


class ClientDetail(LoginRequiredMixin,DetailView):
    model = Client
    template_name = "entrepot/client/client_detail.html"
    

         