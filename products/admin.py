from django.contrib import admin
from .models import Category,SubCategory,Product,ProductReview

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(ProductReview)