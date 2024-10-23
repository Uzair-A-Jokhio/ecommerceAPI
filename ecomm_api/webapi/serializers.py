from .models import Product, Category
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'category', 'name', 'slug', 'description', 
                   'price', 'stock', 'available', 'created_at', 'updated_at']

