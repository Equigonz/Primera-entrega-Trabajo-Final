from http.client import HTTPResponse
from turtle import title
from django.shortcuts import render, redirect
from catalog.models import Books
from catalog.forms import Formulario_create_book


# Create your views here.
def create_book(request):  

    if request.method == "POST":
        form_book = Formulario_create_book(request.POST)

        if form_book.is_valid():
            Books.objects.create(
               title = form_book.cleaned_data["title"],
               book_genre = form_book.cleaned_data["book_genre"]
            )
            return redirect(list_book)
          
    elif request.method == "GET":
        form_book = Formulario_create_book()
        context = {"form_book": form_book}
        return render(request,"create_book.html", context=context)


def list_book(request):
    books = Books.objects.all()
    context = {
        "book":books
    }
    return render(request, "list_book.html", context=context)

def search_books(request):
    search = request.GET['search']
    books = Books.objects.filter(title__icontains=search)
    context = {"books":books}
    return render(request, "search_books.html", context=context)
    
      
