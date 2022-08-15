from django.contrib import admin
from django.urls import path, include 
from catalog.views import create_book, list_book, search_book

urlpatterns = [
    path('admin/', admin.site.urls),       
    path('create_book/', create_book, name = 'create_book'),
    path("list_book/", list_book, name = "list_book" ),
    path("search_book/", search_book, name = "search_book")
]
