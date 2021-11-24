from rest_framework import routers
from django.urls import path, include

from . import views

router = routers.DefaultRouter()
router.register(r'', views.CategoryViewSet)
# router.register
router.register('<slug:category_slug>/', views.CategoryViewSet, basename='category')

# router.register(r'subcategory', views.SubCategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('<slug:category_slug_>/<slug:subcategory_slug>/', views.SubCategoryViewSet.as_view({'get': 'retrieve'}), name='subcategory'),
    path('<slug:category_slug_>/<slug:subcategory_slug>/<slug:subcategoryproduct_slug>/', views.SubCategoryProductViewSet.as_view({'get': 'retrieve'}), name='subcategoryproduct'),
    path('<slug:category_slug_>/<slug:subcategory_slug>/<slug:subcategoryproduct_slug>/<slug:subcategoryproductlast_slug>/', views.SubCategoryProductLastViewSet.as_view({'get': 'retrieve'}), name='subcategoryproductlast')
    # path('posts/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
]
