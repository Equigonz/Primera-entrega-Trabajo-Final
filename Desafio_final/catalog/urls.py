from django.contrib import admin
from django.urls import path
from catalog.views import create_book, list_book

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('create_book/', create_book , name = 'create_book'),
    path("list_book/", list_book, name = "list_book" )
]