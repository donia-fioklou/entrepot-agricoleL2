
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin



class IndexView(View,LoginRequiredMixin):
    def get(self,request):
        return render(request,"base.html")
        
    