from django.shortcuts import render
from django.urls import reverse_lazy
from entrepot.forms.categorie import CategorieForm
from entrepot.models.Categorie import Categorie
from django.core.paginator import Paginator,EmptyPage
from django.views.generic import DetailView,UpdateView,DeleteView

def is_valid_queryparam(param):
    return param != '' and param is not None
def categorie_list_create(request):
    
    form= CategorieForm(request.POST or None)
    if request.method=='POST' and form.is_valid():
        form.save()

    selected="fournisseurs"
    categorie_list=Categorie.objects.all()
    nom=request.GET.get('nom')
    
    if is_valid_queryparam(nom):
        categorie_list=categorie_list.filter(nom=nom)

    
    
    paginator= Paginator(categorie_list.order_by('-dateCreation'),10)
    
    try:
        page= request.GET.get("page")
        if not page:
            page=1
            categorie_list=paginator.page(page)
    except EmptyPage:
        categorie_list=paginator.page(paginator.num_pages())
    return render(request,"entrepot/categorie/categorie_list.html",locals())

class UpdateCategorie(UpdateView):
    model=Categorie
    form_class=CategorieForm
    template_name="entrepot/categorie/categorie_form.html"
    
    def get_success_url(self):
        return reverse_lazy("detail_categories",kwargs={"pk":self.object.pk})

class CategorieDeleteView(DeleteView):
    model = Categorie
    template_name="entrepot/categorie/categorie_confirm_delete.html"
    
    def get_success_url(self):
        return reverse_lazy("categories")



class CategorieDetail(DetailView):
    model = Categorie
    template_name = "entrepot/categorie/categorie_detail.html"