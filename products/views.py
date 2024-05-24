from django.shortcuts import render
from .models import Product,Category,SubCategory

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
    first_category = Category.objects.first()  # Fetch the first category object
    return render(request, 'men.html', {'first_category': first_category})

def women(request):
    second_category = Category.objects.all()[1]  # Fetch the second category object
    return render(request, 'women.html', {'second_category': second_category})


def product_detail(request,p):
    p=Product.objects.get(name=p)
    return render(request,'product-detail.html',context={'p':p})


