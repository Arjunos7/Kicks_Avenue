from django.db import models

class Product(models.Model):

    title=models.CharField(max_length=200)
    price=models.FloatField()
    description=models.TextField()
    size=models.FloatField()
    image = models.ImageField(upload_to='media/')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

