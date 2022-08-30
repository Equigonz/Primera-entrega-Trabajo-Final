from django.contrib import admin
from catalog.models import Books
from catalog.models import Ebooks
from catalog.models import Audiobooks


@admin.register(Audiobooks)
class Audiobooks_admin(admin.ModelAdmin):
    list_display = ["title", "book_genre"]

@admin.register(Books)
class Books_admin(admin.ModelAdmin):
    list_display = ["title", "book_genre"]
    
@admin.register(Ebooks)
class Ebooks_admin(admin.ModelAdmin):
    list_display = ["title", "book_genre"] 
