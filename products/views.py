from django.shortcuts import render

def index(request):
    return render(request,template_name='index.html')

def about(request):
    return render(request,template_name="about.html")



def contact(request):
    return render(request,"contact.html")

def men(request):
    return render(request,'men.html')
def product_detail(request):
    return render(request,'product-detail.html')

def women(request):
    return render(request,'women.html')
