from django.contrib import admin
from django.urls import path, include
from.import views

urlpatterns = [
    path('admin/login', views.admin_login,name="Admin_Login"),
    path('admin/otp_verify', views.admin_otp_verify,name="admin_otp_verify"),
    path('admin/logout', views.admin_logout,name="admin_logout"),
    
]