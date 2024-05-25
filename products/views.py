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
    # Fetch the first category object
    first_category = Category.objects.first()

    # Fetch the subcategories named formals, casuals, and sports
    subcategories = SubCategory.objects.filter(name__in=['formals', 'casuals', 'sports'])

    men_category = Category.objects.get(name='men')
    products = Product.objects.filter(category=men_category)

    # Render the template with the fetched category and subcategories
    return render(request, 'men.html', {
        'first_category': first_category,
        'subcategories': subcategories,
        'products':products
    })

def women(request):
    second_category = Category.objects.all()[1]  # Fetch the second category object

    subcategories=SubCategory.objects.filter(name__in=['Formals', 'Casuals', 'Sports'])

    women_category = Category.objects.get(name='women')
    products = Product.objects.filter(category=women_category)
    return render(request, 'women.html', {
        'second_category': second_category,
        'subcategories':subcategories,
        'products':products
    })


def product_detail(request,p):
    p=Product.objects.get(name=p)
    return render(request,'product-detail.html',context={'p':p})


