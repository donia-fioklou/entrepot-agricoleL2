from django.shortcuts import render
from django.urls import reverse_lazy
from entrepot.decorators import allowed_users
from entrepot.forms.bateau import BateauForm
from entrepot.models.Bateau import Bateau
from django.core.paginator import Paginator,EmptyPage
from django.views.generic import DetailView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
from projetStage.settings import LOGIN_REDIRECT_URL
from django.contrib.auth.mixins import LoginRequiredMixin

def is_valid_queryparam(param):
    return param != '' and param is not None
@login_required
@allowed_users(allowed_roles=['admin'])
def bateau_list_create(request):
    
    form= BateauForm(request.POST or None)
    if request.method=='POST' and form.is_valid():
        form.save()

    selected="fournisseurs"
    bateau_list=Bateau.objects.all()
    nom=request.GET.get('nom')
    
    if is_valid_queryparam(nom):
        bateau_list=bateau_list.filter(nom=nom)

    
    
    paginator= Paginator(bateau_list.order_by('-dateCreation'),10)
    
    try:
        page= request.GET.get("page")
        if not page:
            page=1
            bateau_list=paginator.page(page)
    except EmptyPage:
        bateau_list=paginator.page(paginator.num_pages())
    return render(request,"entrepot/bateau/bateau_list.html",locals())

class UpdateBateau(LoginRequiredMixin,UpdateView):
    model=Bateau
    form_class=BateauForm
    template_name="entrepot/bateau/bateau_form.html"
    
    def get_success_url(self):
        return reverse_lazy("detail_bateaus",kwargs={"pk":self.object.pk})

class BateauDeleteView(LoginRequiredMixin,DeleteView):
    model = Bateau
    template_name="entrepot/bateau/bateau_confirm_delete.html"
    
    def get_success_url(self):
        return reverse_lazy("bateaus")



class BateauDetail(LoginRequiredMixin,DetailView):
    model = Bateau
    template_name = "entrepot/bateau/bateau_detail.html"