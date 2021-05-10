from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    # title =serializers.CharField(max_length=100,blank=False)
    # description=serializers.CharField(max_length=300,blank=True)
    # imageURL=serializers.URLField(max_length=500,blank=False)
    # price=serializers.DecimalField(max_digits=20,decimal_places=2,blank=False)
    # quantity=serializers.IntegerField() 

    class Meta:
        model = Product
        fields = ['id','title','description','imageURL','price','quantity']