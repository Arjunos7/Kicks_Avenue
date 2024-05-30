from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.
def register(request):
    if request.method=="POST":
        u=request.POST['u']
        p=request.POST['p']
        cp=request.POST['cp']
        f=request.POST['f']
        l=request.POST['l']
        e=request.POST['e']
        if p==cp:
            u=User.objects.create_user(username=u,password=p,first_name=f,last_name=l,email=e)
            return redirect('products:index')
        else:
            return HttpResponse('passwords do not match')

    return render(request,template_name="register.html")

def login(request):
    return render(request,"login.html")

