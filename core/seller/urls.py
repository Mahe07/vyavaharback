from.import views
from django.urls import path


urlpatterns = [
    path('login', views.login, name='seller_login'),
    path('login_verification', views.login_verification, name='buyer_login_verification'),
    path('register', views.register, name='seller_register'),
    path('list', views.seller_list, name='seller_list'),
    path('document_verficaton', views.document_verficaton, name='document_verficaton'),
    path('test_mobile',views.test_mobile, name='test_mobile'),
    path('seller_details/<int:userid>',views.seller_details, name='seller_details'),
    path('seller_bankdetails/<int:userid>',views.seller_bankdetails, name='seller_bankdetails'),
    path('edit_bankdetails/<int:userid>/<int:bankid>',views.edit_bankdetails, name='edit_bankdetails'),
    path('edit_details/<int:userid>',views.edit_details, name='edit_details'),
    path('edit_contactdetails/<int:userid>',views.edit_contactdetails, name='edit_contactdetails'),
    path('updatephonenumber/<int:userid>',views.updatephonenumber, name='updatephonenumber'),
    path('updateemail/<int:userid>',views.updateemail, name='updateemail'),
    path('add_ldcdetails/<int:userid>',views.add_ldcdetails, name='add_ldcdetails'),
    path('add_employee/<int:userid>',views.add_employee, name='add_employee'),
]
