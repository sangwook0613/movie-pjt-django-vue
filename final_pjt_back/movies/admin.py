from django.contrib import admin
from .models import Person, Genre, Keyword, Movie
# Register your models here.

@admin.register(Keyword)
class KeywordAdmin(admin.ModelAdmin):
    list_display = ['id', 'keyword_eng_name', 'keyword_count']
    list_display_links = ['id']

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id']

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'eng_name', 'job' ]
    list_display_links = ['id']


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'original_title', ]
    list_display_links = ['id']

