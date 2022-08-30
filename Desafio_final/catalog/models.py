from django.db import models



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
