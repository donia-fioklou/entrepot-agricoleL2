from django.shortcuts import render
from django.urls import reverse_lazy
from entrepot.forms.conteneur import ConteneurForm
from entrepot.models.Conteneur import Conteneur
from django.core.paginator import Paginator,EmptyPage
from django.views.generic import DetailView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
from projetStage.settings import LOGIN_REDIRECT_URL
from django.contrib.auth.mixins import LoginRequiredMixin

def is_valid_queryparam(param):
    return param != '' and param is not None
@login_required
def conteneur_list_create(request):
    
    form= ConteneurForm(request.POST or None)
    if request.method=='POST' and form.is_valid():
        form.save()

    selected="fournisseurs"
    conteneur_list=Conteneur.objects.all()
    nom=request.GET.get('nom')
    
    if is_valid_queryparam(nom):
        conteneur_list=conteneur_list.filter(nom=nom)

    
    
    paginator= Paginator(conteneur_list.order_by('-dateCreation'),10)
    
    try:
        page= request.GET.get("page")
        if not page:
            page=1
            conteneur_list=paginator.page(page)
    except EmptyPage:
        conteneur_list=paginator.page(paginator.num_pages())
    return render(request,"entrepot/conteneur/conteneur_list.html",locals())

class UpdateConteneur(LoginRequiredMixin,UpdateView):
    model=Conteneur
    form_class=ConteneurForm
    template_name="entrepot/conteneur/conteneur_form.html"
    
    def get_success_url(self):
        return reverse_lazy("detail_conteneurs",kwargs={"pk":self.object.pk})

class ConteneurDeleteView(LoginRequiredMixin,DeleteView):
    model = Conteneur
    template_name="entrepot/conteneur/conteneur_confirm_delete.html"
    
    def get_success_url(self):
        return reverse_lazy("conteneurs")



class ConteneurDetail(LoginRequiredMixin,DetailView):
    model = Conteneur
    template_name = "entrepot/conteneur/conteneur_detail.html"