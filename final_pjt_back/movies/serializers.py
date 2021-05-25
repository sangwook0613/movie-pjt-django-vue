from rest_framework import serializers
from .models import Movie, Person, Genre, Keyword
from community.models import Review

# serializers import 안되고 Review 모델은 되길래 community.serializers에 있는거 한번 더 만듬
class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'

class MovieListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = '__all__'

class PeopleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Person
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Genre
        fields = ('name',)

class KeywordSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Keyword
        fields = ('keyword_eng_name',)


class MovieSerializer(serializers.ModelSerializer):
    movie_reviews = ReviewListSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)
    keywords = KeywordSerializer(many=True, read_only=True)
    directors = PeopleSerializer(many=True, read_only=True)
    actors = PeopleSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

class ProfileMovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title', 'original_title', 'poster_path',)


