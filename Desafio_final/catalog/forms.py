from django import forms 

class Formulario_create_book(forms.Form):
      title = forms.CharField(max_length=120)
      book_genre = forms.CharField(max_length=40)

class Formulario_create_ebook(forms.Form):
      title = forms.CharField(max_length=120)
      book_genre = forms.CharField(max_length=40)      
    
class Formulario_create_audiobook(forms.Form):
      title = forms.CharField(max_length=120)
      book_genre = forms.CharField(max_length=40)   
        
  