from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from .models import Movie, Person
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


class MovieSerializer(serializers.ModelSerializer):
    movie_reviews = ReviewListSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

class ProfileMovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title', 'original_title', 'poster_path',)


class PeopleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Person
        fields = '__all__'