from django.contrib import admin
from .models import *

class SubCategoryTabularInline( admin.TabularInline):
    model = Subcategory
    ordering = ['id']
    prepopulated_fields = {"slug": ("name",)}

class SubCategoryProductTabularInline( admin.TabularInline):
    model = SubcategoryProduct
    ordering = ['id']
    prepopulated_fields = {"slug": ("name",)}

class SubCategoryProductLastTabularInline( admin.TabularInline):
    model = SubcategoryProductLast
    ordering = ['id']
    prepopulated_fields = {"slug": ("name",)}
