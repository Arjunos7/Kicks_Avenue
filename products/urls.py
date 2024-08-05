from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
app_name="products"
urlpatterns = [
    path('',views.index,name='index'),
    path('allproducts/',views.allproducts,name='allproducts'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('men/',views.men,name='men'),
    path('products/men/<str:category>/', views.men_product_list, name='men_product_list'),
    path('products/women/<str:category>/', views.women_product_list, name='women_product_list'),
    path('women/',views.women,name='women'),
    path('product_detail/<str:p>',views.product_detail,name='product_detail'),

]