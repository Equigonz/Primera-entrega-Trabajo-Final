from django.contrib import admin
from django.urls import path, include
from Desafio_final.views import template_con_lista 
from catalog.views import create_book

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('template_con_lista/', template_con_lista , name = 'template_con_lista'),
    path('create_book/', create_book, name = 'create_book')
]
