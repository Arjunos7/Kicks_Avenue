from django.db import models
from django.contrib.auth.models import User

RATING=(
    (1,"★☆☆☆☆"),
    (2,"★★☆☆☆"),
    (3,"★★★☆☆"),
    (4,"★★★★☆"),
    (5,"★★★★★"),
)

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/categories/', blank=True, null=True)  # Add this line

    def __str__(self):
        return self.name

# Sub Category (e.g., Formals, Casuals, Sports)
class SubCategory(models.Model):
    category = models.ForeignKey(Category, related_name='subcategories', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/subcategories/', blank=True, null=True)  # Add this line

    def __str__(self):
        return self.name

# Product (e.g., specific shoes)
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='menwomen', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='images/products/')
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class ProductReview(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,related_name="reviews")
    review=models.TextField()
    rating=models.IntegerField(choices=RATING,default=None)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name

    def get_rating(self):
        return self.rating
