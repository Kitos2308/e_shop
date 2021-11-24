from django.db import models
from api.category.models import SubcategoryProductLast, Subcategory, SubcategoryProduct
# Create your models here.
from .utils import UploadTo
from django.utils.safestring import mark_safe

class Brand(models.Model):
    brand_name = models.CharField(max_length=50)
    brand_description = models.CharField(max_length=150)

    def __str__(self):
        return self.brand_name

    class Meta:
        db_table = 'brand'


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    price = models.CharField(max_length=50)
    stock = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True, blank=True)
    image = models.FileField(upload_to=UploadTo('image'),
                                 max_length=255, null=True, blank=True)
    subcategoryproductlast = models.ForeignKey(
        SubcategoryProductLast, on_delete=models.SET_NULL, blank=True, null=True, related_name='product')

    subcategoryproduct = models.ForeignKey(
        SubcategoryProduct, on_delete=models.SET_NULL, blank=True, null=True, related_name='subcategory_product')

    product_brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, blank=True, null=True,
                                      related_name='product_brand')

    soldout = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'product'

    def thumbnail_image(self):
        if self.image:
            return mark_safe('<img src="{url}" width="{width}" />'.format(
                url=self.image.url,
                width=300,
            ))
        else:
            return 'NO IMAGE'

    thumbnail_image.short_description = 'Thumbnail image product url'


