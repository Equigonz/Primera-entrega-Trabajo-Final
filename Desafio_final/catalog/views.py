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
            title = form.cleaned_data["title"],
            book_genre = form.cleaned_data["book_genre"]
           )
           return redirect(list_book)
          
       elif request.method == "GET":
             form_book = Formulario_create_book()
             context = {"form_book": form_book}
             return render(request,"new_book.html", context=context)




  #original "create_book"
   # new_book = Books.objects.create(title = "El Alquimista", 
    #book_genre = "Autoayuda")
    #context = {
    #    "new_book": new_book
    #}
    #return render(request,"new_book.html", context=context)


def list_book(request):
    books = Books.objects.all()
    context = {
        "book":books
    }
    return render(request, "list_book.html", context=context)
    