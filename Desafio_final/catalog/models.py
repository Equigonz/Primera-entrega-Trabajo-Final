from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=120)
    book_genre = models.CharField(max_length=40)

class Audiobooks(models.Model):
    title = models.CharField(max_length=120)
    book_genre = models.CharField(max_length=40)   

class Ebooks(models.Model):
    title = models.CharField(max_length=120)
    book_genre = models.CharField(max_length=40)     