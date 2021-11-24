from django.db import models
from django.urls import reverse
from uuid import uuid4
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # url = models.CharField(unique=True, max_length=20, null=False, default=uuid4())
    slug = models.SlugField(max_length=255, unique=True, )
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})


class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True,
                                 related_name= 'subcategory')
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # url = models.CharField(unique=True, max_length=20, null=False, default=uuid4())
    slug = models.SlugField(max_length=255, unique=True,)
    class Meta:
        db_table = 'subcategory'

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('subcategory', kwargs={'subcategory_slug': self.slug, 'category_slug_':self.category.slug})




class SubcategoryProduct(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True,
                                 related_name='category')
    subcategory = models.ForeignKey(Subcategory, on_delete=models.SET_NULL, blank=True, null=True,
                                    related_name='subcategoryproduct')
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255, unique=True,)
    class Meta:
        db_table = 'subcategory_product'

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('subcategory_product', kwargs={'subcategoryproduct_slug': self.slug})


class SubcategoryProductLast(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True,
                                 related_name='subcategoryproduct_category_last')
    subcategory = models.ForeignKey(SubcategoryProduct, on_delete=models.SET_NULL, blank=True, null=True,
                                    related_name='subcategoryproduct_last')
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255, unique=True,)
    class Meta:
        db_table = 'subcategory_product_last'

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('subcategory_product_last', kwargs={'subcategoryproductlast_slug': self.slug})