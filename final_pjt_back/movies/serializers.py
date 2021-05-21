from rest_framework import serializers
from .models import Movie, Person, Genre, Keyword



class MovieListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = '__all__'

class ProfileMovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title', 'original_title')


class PeopleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Person
        fields = '__all__'