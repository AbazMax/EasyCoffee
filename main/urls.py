from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('about/', views.about),
    path('products/', views.pruducts),
    path('contacts/', views.contacts)
]