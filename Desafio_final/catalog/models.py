from django.db import models

# genero 3 modelos que vamos a vender

class Books(models.Model):
    title = models.CharField(max_length=120)
    book_genre = models.CharField(max_length=40)   

    def __str__(self):
        return self.title

class Ebooks(models.Model):
    title = models.CharField(max_length=120)
    book_genre = models.CharField(max_length=40)

    def __str__(self):
        return self.title
            
class Audiobooks(models.Model):
    title = models.CharField(max_length=120)
    book_genre = models.CharField(max_length=40)

    def __str__(self):
        return self.title
