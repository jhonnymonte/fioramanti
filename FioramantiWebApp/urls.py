from django.urls import path
from FioramantiWebApp import views

urlpatterns = [
    path('',views.home,name='Home'),
    path('servicios',views.servicios,name='Servicios'),
    path('blog',views.blog,name='Blog'),
    path('contacto',views.contacto,name='Contacto'),
]
