from django.contrib import admin
from django.urls import path, include 
from catalog.views import create_book, list_book, list_ebook,list_audiobook, search_books, create_ebook, create_audiobook

urlpatterns = [
    path('admin/', admin.site.urls),       
    path('create_book/', create_book, name = 'create_book'),
    path("list_book/", list_book, name = "list_book" ),
    path("search_books/", search_books, name = "search_books"),
    path('create_ebook/', create_ebook, name = 'create_ebook'),
    path('create_audiobook/', create_audiobook, name = 'create_audiobook'),
    path("list_ebook/", list_ebook, name = "list_ebook" ),
    path("list_audiobook/", list_audiobook, name = "list_audiobook" )
]
