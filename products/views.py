from django.shortcuts import render
from .models import Product

def index(request):
    c=Product.objects.all()
    return render(request,template_name='index.html',context={'c':c})

def allproducts(request):
    c = Product.objects.all()
    return render(request,template_name="allproducts.html",context={'c':c})

def about(request):
    return render(request,template_name="about.html")



def contact(request):
    return render(request,"contact.html")

def men(request):
    return render(request,'men.html')
def product_detail(request,p):
    p=Product.objects.get(name=p)
    return render(request,'product-detail.html',context={'p':p})

def women(request):
    return render(request,'women.html')


