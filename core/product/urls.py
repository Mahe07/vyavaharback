"""vyavhar_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns
from.import views

urlpatterns = [
    path( 'category',views.category, name='category'),
    path('list', views.product_list, name='product_list'),
    path('upload', views.upload, name='upload'),
    path('sku', views.sku, name='Check SKU'),

    path('seller_product', views.seller_product, name='seller_product'),
    path('status/<int:pk>', views.product_status, name='product_status'),
    path('inventory/<int:seller_id>', views.inventory, name='inventory'),
    path('inventory/update', views.inventory_update, name='inventory_update'),
    path('single_product/<int:product_id>',views.single_product,name="single_product"),
    path('products_count', views.products_count, name='products_count'),
    path('approved_productscount', views.approved_productscount, name='approved_productscount'),
    path('pending_productscount', views.pending_productscount, name='pending_productscount'),
    path('draft_productscount', views.draft_productscount, name='draft_productscount'),
    path('declined_productscount', views.declined_productscount, name='declined_productscount'),
    path('all_products', views.all_products, name='all_products'),
    path('approved_products', views.approved_products, name='approved_products'),
    path('pending_products', views.pending_products, name='pending_products'),
    path('draft_products', views.draft_products, name='draft_products'),
    path('declined_products', views.declined_products, name='declined_products'),
    path('inventory_count', views.inventory_count, name='inventory_count'),
    path('lowstock_count', views.lowstock_count, name='low_count'),
    path('outofstock_count', views.outofstock_count, name='outofstock_count'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
