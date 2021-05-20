from django.db import models
from django.conf import settings
# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
'''
class Actor(models.Model):
    actor_name = models.CharField(max_length=50)
    actor_eng_name = models.CharField(max_length=50)
    actor_profile_path = models.CharField(max_length=200)
    actor_gender = models.IntegerField()

    def __str__(self):
        return self.actor_name

class Director(models.Model):
    director_name = models.CharField(max_length=50)
    director_eng_name = models.CharField(max_length=50)
    director_profile_path = models.CharField(max_length=200)
    director_gender = models.IntegerField()
    
    def __str__(self):
        return self.director_name
'''
class Person(models.Model):
    name = models.CharField(max_length=50)
    eng_name = models.CharField(max_length=50)
    profile_path = models.CharField(max_length=200)
    gender = models.IntegerField()
    job = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Keyword(models.Model):
    keyword_name = models.CharField(max_length=50, blank=True)
    keyword_eng_name = models.CharField(max_length=50)
    keyword_count = models.IntegerField(blank=True, default=1)

    def __str__(self):
        return self.keyword_eng_name


class Movie(models.Model):
    title = models.CharField(max_length=50)
    original_title = models.CharField(max_length=50)
    overview = models.TextField()
    release_date = models.DateField()
    poster_path = models.CharField(max_length=200)
    backdrop_path = models.CharField(max_length=200)
    runtime = models.IntegerField(default=0)
    genres = models.ManyToManyField(Genre)
    actors = models.ManyToManyField(Person, related_name='movie_actor')
    directors = models.ManyToManyField(Person, related_name='movie_director')
    keywords = models.ManyToManyField(Keyword)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    hates = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='hate_movies')

    def __str__(self):
        return self.title
