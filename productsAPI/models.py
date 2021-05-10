from django.db import models

# Create your models here.

class Product(models.Model):
    id=models.IntegerField(primary_key=True)
    title =models.CharField(max_length=100,blank=False)
    description=models.CharField(max_length=300,blank=True)
    imageURL=models.URLField(max_length=500,blank=False)
    price=models.DecimalField(max_digits=20,decimal_places=2,blank=False)
    quantity=models.IntegerField() 

    def __str__(self):
        return f'Product: {self.title}\nDescription:{self.description}'