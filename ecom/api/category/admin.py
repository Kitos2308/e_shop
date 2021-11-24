from django.contrib import admin
from .models import *
# Register your models here.
from django.contrib.auth.models import Permission
from .models import *
from .inline_models import *




@admin.register(Category)
class ProductAdmin(admin.ModelAdmin ):
    inlines = [SubCategoryTabularInline, SubCategoryProductTabularInline, SubCategoryProductLastTabularInline ]
    list_display = ('__str__', 'description')
    prepopulated_fields = {"slug": ("name",)}


    ordering = ['id', ]

    fieldsets = (
        (None, {
            'fields': ( 'name', 'description', 'slug')
        }),

    )

# @admin.register(Subcategory)
# class ProductAdmin(admin.ModelAdmin ):
#     list_display = ('__str__', 'category', )
#
#
#     ordering = ['id', ]
#
#     fieldsets = (
#         (None, {
#             'fields': ('category', 'name', 'description',)
#         }),
#
#     )