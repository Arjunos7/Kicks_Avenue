from django.shortcuts import render

def index(request):
    return render(request,template_name='index.html')

def about(request):
    return render(request,template_name="about.html")

def cart(request):
    return render(request,"cart.html")

def checkout(request):
    return render(request,"checkout.html")
def contact(request):
    return render(request,"contact.html")

