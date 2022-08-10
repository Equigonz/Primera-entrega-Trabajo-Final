from turtle import title
from django.shortcuts import render
from catalog.models import Books, Audiobooks, Ebooks

# Create your views here.
def create_book(request):  
    new_book = Books.objects.create(title = "El Principito", 
    book_genre = "aventura", author = "Antoine de Saint-Exupèry")
    context = {
        "new_book": new_book
    }
    return render(request,"new_book.html", context=context)