from.import views
from django.urls import path


urlpatterns = [
    path('login', views.login),
    path('login_verification', views.login_verification, name='buyer_login_verification'),
    path('register', views.register, name='buyer_register'),
    path('logout', views.register, name='buyer_register'),
    path('list', views.buyer_list, name='buyer_list'),
    path('document_verficaton', views.document_verficaton, name='document_verficaton'),
    path('add_businessinfo', views.add_businessinfo, name='add_businessinfo'),
]
