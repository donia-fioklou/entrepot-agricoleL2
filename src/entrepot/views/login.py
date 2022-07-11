from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.shortcuts import render,redirect

def login_user(request):
        if request.method=="POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                messages.success(request,("nom d'utilisateur ou mot de passe incorrecte"))
                return redirect('login')
        

        else:
        
            return render(request,'authenticate/login.html',{})