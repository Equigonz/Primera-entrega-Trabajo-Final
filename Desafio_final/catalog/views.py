from turtle import title
from django.shortcuts import render
from catalog.models import Books


# Create your views here.
def create_book(request):  
    new_book = Books.objects.create(title = "El Principito", 
    book_genre = "aventura")
    context = {
        "new_book": new_book
    }
    return render(request,"new_book.html", context=context)


def list_book(request):
    books = Books.objects.all()
    context = {
        "book":books
    }
    return render(request, "list_book.html", context=context)
    