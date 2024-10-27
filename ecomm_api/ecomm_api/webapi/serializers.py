from .models import Product, Category, Brand
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Product
        fields = '__all__'
