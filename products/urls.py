from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
app_name="products"
urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('men/',views.men,name='men'),
    path('women/',views.women,name='women'),
    path('product_detail/',views.product_detail,name='product_detail'),

]