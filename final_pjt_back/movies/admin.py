from django.contrib import admin
from .models import Actor, Director, Genre, Keyword, Movie
# Register your models here.

@admin.register(Keyword)
class KeywordAdmin(admin.ModelAdmin):
    list_display = ['id', 'keyword_eng_name', 'keyword_count']
    list_display_links = ['id']

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id']

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ['id', 'actor_name', 'actor_eng_name', ]
    list_display_links = ['id']

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ['id', 'director_name', 'director_eng_name', ]
    list_display_links = ['id']

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'original_title', ]
    list_display_links = ['id']

