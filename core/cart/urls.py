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
    path('add_to_cart', views.add_to_cart, name='add_to_cart'),
    path('cart_list/<int:id>', views.cart_list, name='cart_list'),
    path('cart_count/<int:id>', views.cart_count, name='cart_count'),
    path('cart_delete/<int:id>', views.cart_delete, name='cart_delete'),
    path('cart_total/<int:id>', views.cart_total, name='cart_total'),


]

