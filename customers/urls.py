from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from . import views
app_name="customers"

urlpatterns = [
    path("register/",views.register,name="register"),
    path("login/",views.login,name="login"),


]