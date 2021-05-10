from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .models import Product
from django.views.decorators.csrf import csrf_exempt
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

def index(request):
    return HttpResponse("this is homepage.. try localhost:8000/products")


@csrf_exempt 
@api_view(['GET', 'POST'])
def product_list(request):
    if request.method=='GET':
        productDetails = Product.objects.all()
        serializer = ProductSerializer(productDetails, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        # data = JSONParser().parse(request)
        serializer = ProductSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            # return JsonResponse(serializer.data, status=201)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   

@csrf_exempt
@api_view(['GET', 'DELETE','PUT'])
def productDetails(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    
    except Product.DoesNotExist:
        return HttpResponse(status=404)

    if request.method=='GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    elif request.method =='PUT':
        # data = JSONParser().parse(request)
        serializer = ProductSerializer(product, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        pro_name = product.title
        product.delete()
        return Response({'message': 'Product {0} was deleted successfully!'.format(pro_name)},status=status.HTTP_204_NO_CONTENT)