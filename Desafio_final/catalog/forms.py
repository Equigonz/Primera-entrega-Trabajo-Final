from django import forms 

class Formulario_create_book(forms.Form):
      title = forms.CharField(max_length=120)
      book_genre = forms.CharField(max_length=40)
    
    
    #  Class Book
    #  title = models.CharField(max_length=120)
    #  book_genre = models.CharField(max_length=40)