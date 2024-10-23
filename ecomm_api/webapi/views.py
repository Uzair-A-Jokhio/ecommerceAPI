from django.shortcuts import render
from rest_framework import generics
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class ProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def get_permissions(self):
        permission_classes = []

        if self.request.method != "GET":
            permission_classes = [IsAuthenticated]
        
        return [permission() for permission in permission_classes]

class SingleProductView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    search_fields = ['category__title']
    ordering_fields = ['price', 'inventory']
    def get_permissions(self):
        permission_classes = []

        if self.request.method != "GET":
            permission_classes = [IsAuthenticated]
        
        return [permission() for permission in permission_classes]

