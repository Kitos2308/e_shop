from django.contrib import admin
from .models import Product, Brand
# Register your models here.
from django.contrib.auth.models import Permission


admin.site.register(Permission)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin ):
    list_display = ('__str__', 'brand_description')



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin ):
    list_display = ('__str__', 'description', 'price')

    readonly_fields = ( 'thumbnail_image', )

    ordering = ['id', ]

    fieldsets = (
        (None, {
            'fields': ( 'name', 'description', 'price', 'stock', 'is_active',  'product_brand', 'subcategoryproductlast',
                       'subcategoryproduct', )
        }),
        ('Images', {
            'fields': (
                ('image', 'thumbnail_image'),
                ),
        }),
    )