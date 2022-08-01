from unicodedata import name
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from entrepot.decorators import allowed_users
from entrepot.forms.zone import ZoneForm
from entrepot.models.Zone import Zone
from django.core.paginator import Paginator,EmptyPage
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import DetailView,ListView
from django.contrib.auth.decorators import login_required
from projetStage.settings import LOGIN_REDIRECT_URL
from django.contrib.auth.mixins import LoginRequiredMixin
def is_valid_queryparam(param):
    return param != '' and param is not None
@login_required
@allowed_users(allowed_roles=['admin','quai'])
def zone_list_create(request):
    
    form= ZoneForm(request.POST or None)
    if request.method=='POST' and form.is_valid():
        form.save()
        form=ZoneForm()

    selected="zones"
    zone_list=Zone.objects.all()
    nom=request.GET.get('nom')
    qteMax=request.GET.get('qteMax')
    
    if is_valid_queryparam(nom):
        zone_list=zone_list.filter(nom=nom)
    elif is_valid_queryparam(qteMax):
        zone_list=zone_list.filter(qteMax=qteMax)
        
    
    
    
    paginator= Paginator(zone_list.order_by('-dateCreation'),10)
    
    try:
        page= request.GET.get("page")
        if not page:
            page=1
            zone_list=paginator.page(page)
    except EmptyPage:
        zone_list=paginator.page(paginator.num_pages())
    return render(request,"entrepot/zone/zone_list.html",locals())




"""
class CreateZone(CreateView):
    model=Zone
    form_class=ZoneForm
    template_name="entrepot/zone/zone_form.html"
    
    def get_success_url(self):
        return reverse_lazy("detail_zones",kwargs={"pk":self.object.pk})
"""

class UpdateZone(LoginRequiredMixin,UpdateView):
    model=Zone
    form_class=ZoneForm
    template_name="entrepot/zone/zone_form.html"
    
    def get_success_url(self):
        return reverse_lazy("detail_zones",kwargs={"pk":self.object.pk})
    
class ZoneDeleteView(LoginRequiredMixin,DeleteView):
    model = Zone
    template_name="entrepot/zone/zone_confirm_delete.html"
    
    def get_success_url(self):
        return reverse_lazy("zones")


class ZoneDetail(LoginRequiredMixin,DetailView):
    model = Zone
    template_name = "entrepot/zone/zone_detail.html"
    

         