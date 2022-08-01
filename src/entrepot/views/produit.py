from django.shortcuts import render
from django.urls import reverse_lazy
from entrepot.decorators import allowed_users
from entrepot.forms.produit import ProduitForm
from entrepot.models.Produit import Produit
from django.core.paginator import Paginator,EmptyPage
from django.views.generic import DetailView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
from projetStage.settings import LOGIN_REDIRECT_URL
from django.contrib.auth.mixins import LoginRequiredMixin

def is_valid_queryparam(param):
    return param != '' and param is not None
@login_required
@allowed_users(allowed_roles=['admin'])
def produit_list_create(request):
    
    form= ProduitForm(request.POST or None)
    if request.method=='POST' and form.is_valid():
        form.save()

    
    produit_list=Produit.objects.all()
    nomProd=request.GET.get('nomProd')
    
    if is_valid_queryparam(nomProd):
        produit_list=produit_list.filter(nomProd=nomProd)
    
    
    paginator= Paginator(produit_list.order_by('-dateCreation'),10)
    
    try:
        page= request.GET.get("page")
        if not page:
            page=1
            produit_list=paginator.page(page)
    except EmptyPage:
        produit_list=paginator.page(paginator.num_pages())
    return render(request,"entrepot/produit/produit_list.html",locals())

class UpdateProduit(LoginRequiredMixin,UpdateView):
    model=Produit
    form_class=ProduitForm
    template_name="entrepot/produit/produit_form.html"
    
    def get_success_url(self):
        return reverse_lazy("detail_produits",kwargs={"pk":self.object.pk})

class ProduitDeleteView(LoginRequiredMixin,DeleteView):
    model = Produit
    template_name="entrepot/produit/produit_confirm_delete.html"
    
    def get_success_url(self):
        return reverse_lazy("produits")

class ProduitDetail(LoginRequiredMixin,DetailView):
    model = Produit
    template_name = "entrepot/produit/produit_detail.html"