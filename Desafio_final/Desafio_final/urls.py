from django.contrib import admin
from django.urls import path, include
from Desafio_final.views import  new_book

urlpatterns = [
    path('admin/', admin.site.urls),    
    path("new_book/", new_book , name = "new_book")
]
