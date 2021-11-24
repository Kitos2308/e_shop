from rest_framework import serializers
from ..product.serializers import ProductSerializer

from .models import *

class SubCategoryProductSerializerLast(serializers.ModelSerializer):
    product = ProductSerializer(many=True)
    class Meta:
        model = SubcategoryProductLast
        fields = ('name', 'slug', 'description', 'product')


class SubCategoryProductSerializer(serializers.ModelSerializer):
    subcategoryproduct_last =SubCategoryProductSerializerLast(many=True)
    subcategory_product = ProductSerializer(many=True)
    class Meta:
        model = SubcategoryProduct
        fields = ('id','name', 'slug', 'description', 'subcategory_product', 'subcategoryproduct_last')


class SubCategorySerializer(serializers.ModelSerializer):
    subcategoryproduct = SubCategoryProductSerializer(many=True)
    class Meta:
        model = Subcategory
        fields = ('id', 'name','slug', 'description', 'subcategoryproduct')


class CategorySerializer(serializers.ModelSerializer):
    subcategory = SubCategorySerializer(many=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'description', 'subcategory')


class CategorySerializerSingle(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'subcategory')


