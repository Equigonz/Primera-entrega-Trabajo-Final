from gettext import Catalog
from http.client import HTTPResponse
from multiprocessing import context
from turtle import title
from django.shortcuts import render, redirect
from catalog.models import Books, Ebooks, Audiobooks
from catalog.forms import Formulario_create_book, Formulario_create_ebook, Formulario_create_audiobook
from django.views.generic import DetailView 
from django.contrib.auth.decorators import login_required





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
        return render(request,"CreateAndDelete/create_book.html", context=context)

@login_required
def list_book(request):
    books = Books.objects.all()
    context = {
        "book":books
    }
    return render(request, "Catalog_List/list_book.html", context=context)


def list_ebook(request):
    ebooks = Ebooks.objects.all()
    context = {
        "ebook":ebooks
    }
    return render(request, "Catalog_List/list_ebook.html", context=context)   
    
def list_audiobook(request):
    audiobooks = Audiobooks.objects.all()
    context = {
        "audiobook":audiobooks
    }
    return render(request, "Catalog_List/list_audiobook.html", context=context)    

def search_books(request):
    search = request.GET["search"]
    books = Books.objects.filter(title__icontains = search)
    ebooks = Ebooks.objects.filter(title__icontains = search)
    audiobooks = Audiobooks.objects.filter(title__icontains = search)
    context = {
        "books":books,
        "ebooks":ebooks,
        "audiobooks":audiobooks
        }
    return render(request, "search_books.html", context=context)



def create_ebook(request):  

    if request.method == "POST":
        form_ebook = Formulario_create_ebook(request.POST)

        if form_ebook.is_valid():
            Ebooks.objects.create(
               title = form_ebook.cleaned_data["title"],
               book_genre = form_ebook.cleaned_data["book_genre"]
            )
            return redirect(list_ebook)

    elif request.method == "GET":
        form_ebook = Formulario_create_ebook()
        context = {"form_ebook": form_ebook}
        return render(request,"CreateAndDelete/create_ebook.html", context=context)        
    
def create_audiobook(request):  

    if request.method == "POST":
        form_audiobook = Formulario_create_audiobook(request.POST)

        if form_audiobook.is_valid():
            Audiobooks.objects.create(
               title = form_audiobook.cleaned_data["title"],
               book_genre = form_audiobook.cleaned_data["book_genre"]
            )
            return redirect(list_audiobook)   

    elif request.method == "GET":
        form_audiobook = Formulario_create_audiobook()
        context = {"form_audiobook": form_audiobook}
        return render(request,"CreateAndDelete/create_audiobook.html", context=context)           

def delete_book(request, pk):
    if request.method == 'GET':
        book = Books.objects.get(pk=pk)
        context = {'book':book}
        return render(request, 'CreateAndDelete/delete_book.html', context=context)
    elif request.method == 'POST':
        book = Books.objects.get(pk=pk)
        book.delete()
        return redirect(list_book)          

def delete_ebook(request, pk):
    if request.method == 'GET':
        ebook = Ebooks.objects.get(pk=pk)
        context = {'ebook':ebook}
        return render(request, 'CreateAndDelete/delete_ebook.html', context=context)
    elif request.method == 'POST':
        ebook = Ebooks.objects.get(pk=pk)
        ebook.delete()
        return redirect(list_ebook)  

def delete_audiobook(request, pk):
    if request.method == 'GET':
        audiobook = Audiobooks.objects.get(pk=pk)
        context = {'audiobook':audiobook}
        return render(request, 'CreateAndDelete/delete_audiobook.html', context=context)
    elif request.method == 'POST':
        audiobook = Audiobooks.objects.get(pk=pk)
        audiobook.delete()
        return redirect(list_audiobook)   

def update_book(request, pk):
    if request.method == 'POST':
        
        form_book = Formulario_create_book(request.POST)
        if form_book.is_valid():
            book = Books.objects.get(id=pk)
            book.title = form_book.cleaned_data['title']
            book.book_genre = form_book.cleaned_data['book_genre']
            book.save()

            return redirect(list_book)

    elif request.method == 'GET':
        book = Books.objects.get(id=pk)
    
        form_book = Formulario_create_book(initial={'title':book.title, 'book_genre':book.book_genre})
        context = {'form_book': form_book}
        
        return render(request, 'Update/update_book.html', context = context)

def update_ebook(request, pk):
    if request.method == 'POST':
        
        form_ebook = Formulario_create_ebook(request.POST)
        if form_ebook.is_valid():
            ebook = Ebooks.objects.get(id=pk)
            ebook.title = form_ebook.cleaned_data['title']
            ebook.book_genre = form_ebook.cleaned_data['book_genre']
            ebook.save()

            return redirect(list_ebook)

    elif request.method == 'GET':
        ebook = Ebooks.objects.get(id=pk)
    
        form_ebook = Formulario_create_ebook(initial={'title':ebook.title, 'book_genre':ebook.book_genre})
        context = {'form_ebook': form_ebook}
        
        return render(request, 'Update/update_ebook.html', context = context)

def update_audiobook(request, pk):
    if request.method == 'POST':
        
        form_audiobook = Formulario_create_audiobook(request.POST)
        if form_audiobook.is_valid():
            audiobook = Audiobooks.objects.get(id=pk)
            audiobook.title = form_audiobook.cleaned_data['title']
            audiobook.book_genre = form_audiobook.cleaned_data['book_genre']
            audiobook.save()

            return redirect(list_audiobook)

    elif request.method == 'GET':
        audiobook = Audiobooks.objects.get(id=pk)
    
        form_audiobook = Formulario_create_audiobook(initial={'title':audiobook.title, 'book_genre':audiobook.book_genre})
        context = {'form_audiobook': form_audiobook}
        
        return render(request, 'Update/update_audiobook.html', context = context)

def index(request):
    return render(request, 'index.html')  
  
        

class Detail_books(DetailView):
    model = Books
    template_title = "detail_books.html"
    context_object_title = "listado"

