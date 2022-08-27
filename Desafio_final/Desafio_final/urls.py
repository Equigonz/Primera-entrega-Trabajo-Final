from django.contrib import admin
from django.urls import path, include
from users.views import login_request, register
from catalog.views import create_book, list_book, list_ebook,list_audiobook, search_books, create_ebook, create_audiobook, delete_book, delete_ebook, delete_audiobook, update_book, update_ebook, update_audiobook, index, Detail_books
urlpatterns = [

    path('admin/', admin.site.urls),
    path('', index, name='index'),        
    path('create_book/', create_book, name = 'create_book'),
    path("list_book/", list_book, name = "list_book" ),
    path("search_books/", search_books, name = "search_books"),
    path('create_ebook/', create_ebook, name = 'create_ebook'),
    path('create_audiobook/', create_audiobook, name = 'create_audiobook'),
    path("list_ebook/", list_ebook, name = "list_ebook" ),
    path("list_audiobook/", list_audiobook, name = "list_audiobook" ),
    path("delete_book/<int:pk>/", delete_book, name = 'delete_book'),
    path('delete_ebook/<int:pk>/', delete_ebook, name = 'delete_ebook'),
    path('delete_audiobook/<int:pk>/', delete_audiobook, name = 'delete_audiobook'),
    path('update_book/<int:pk>/', update_book, name = 'update_book'),
    path('update_ebook/<int:pk>/', update_ebook, name = 'update_ebook'),
    path('update_audiobook/<int:pk>/', update_audiobook, name = 'update_audiobook'),
    path("detail_books/", Detail_books.as_view(), name = "detail_books"),
    path("login/", login_request, name = "login"),
    path("register/", register, name = "Register")
    ]
