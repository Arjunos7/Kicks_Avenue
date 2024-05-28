from django.shortcuts import render,redirect
from django.contrib.auth import logout

# Create your views here.
def register(request):
    return render(request,"register.html")
def login(request):
    return render(request,"login.html")

