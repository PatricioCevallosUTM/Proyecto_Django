from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name="base"),
    path('sample/', views.sample, name="sample"),
    path('nosotros/', views.nosotros, name="nosotros"),
    path('articulos/', views.articulos, name="articulos"),
    path('contacto/', views.contacto, name="contacto"),
    
]