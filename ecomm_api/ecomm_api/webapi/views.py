from django.shortcuts import render
from rest_framework import generics
from .models import Product, Category, Brand
from .serializers import ProductSerializer, CategorySerializer , BrandSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class ProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

class SingleProductView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class BrandView(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer