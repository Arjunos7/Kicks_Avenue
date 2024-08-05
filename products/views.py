from django.shortcuts import render, redirect
from .models import Product,Category,SubCategory,ProductReview
from .forms import ProductReviewForm
from django.contrib.auth.models import User
from django.http import HttpResponse,JsonResponse


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


    return render(request, 'men.html', {
        'first_category': first_category,
        'subcategories': subcategories,
        'products':products
    })



def men_product_list(request, category):
    men_category = Category.objects.get(name='men')  # Fetching the men category
    subcategories = SubCategory.objects.filter(category=men_category)  # Filtering subcategories belonging to the men category
    products = Product.objects.filter(category=men_category, subcategory__name=category)  # Filtering products belonging to the 'men' category and the specified subcategory name
    return render(request, 'men_product_list.html', {'products': products, 'category': category})

def women_product_list(request, category):
    women_category = Category.objects.get(name='women')  # Fetching the men category
    subcategories = SubCategory.objects.filter(category=women_category)  # filter subcategories belonging to the men category
    products = Product.objects.filter(category=women_category, subcategory__name=category)  # Filtering products belonging to the MEN category and the specified subcategory name
    return render(request, 'women_product_list.html', {'products': products, 'category': category})


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




def product_detail(request, p):
    # Fetch the product by name
    p = Product.objects.get(name=p)

    # Fetch the reviews related to this product, ordered by date
    reviews = ProductReview.objects.filter(product=p).order_by("-date")

    if request.method == 'POST':
        # Handle form submission
        review_form = ProductReviewForm(request.POST)
        if review_form.is_valid():
            # Save the form data but don't commit to the database yet
            new_review = review_form.save(commit=False)
            # Assign the product and the user to the review
            new_review.product = p
            new_review.user = request.user
            # Save the review to the database
            new_review.save()
            # Redirect to the same product detail page
            return redirect('products:product_detail', p=p.name)
    else:
        # If it's a GET request, create a blank form
        review_form = ProductReviewForm()

    # Precompute star ratings
    rating_data = []
    for r in reviews:
        rating_data.append({
            'user': r.user.username,
            'date': r.date,
            'review': r.review,
            'rating': r.rating
        })

    return render(request, 'product-detail.html', {
        'p': p,
        'reviews': rating_data,
        'review_form': review_form
    })
