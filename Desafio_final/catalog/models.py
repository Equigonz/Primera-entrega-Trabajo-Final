from django.db import models

# genero 3 modelos que vamos a vender
class Books(models.Model):
    title = models.CharField(max_length=120)
    book_genre = models.CharField(max_length=40)
    
# class Audiobooks(models.Model):
#     title = models.CharField(max_length=120)
#     book_genre = models.CharField(max_length=40)  
    

# class Ebooks(models.Model):
#     title = models.CharField(max_length=120)
#     book_genre = models.CharField(max_length=40)
        
