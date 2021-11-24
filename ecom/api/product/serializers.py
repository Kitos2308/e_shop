from rest_framework import serializers

from .models import Product, Brand


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('brand_name',  )


class ProductSerializer(serializers.ModelSerializer):

    image = serializers.ImageField(
        max_length=None, allow_empty_file=False, allow_null=True, required=False)
    product_brand = BrandSerializer(read_only=True)
    class Meta:

        model = Product
        fields = ('id', 'name', 'description', 'price', 'image', 'soldout',  'product_brand')
