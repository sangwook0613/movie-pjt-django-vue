from rest_framework import serializers
from .models import Movie, Person, Genre, Keyword
from community.models import Review, Comment
from django.contrib.auth import get_user_model
User = get_user_model()


# serializers import 안되고 Review 모델은 되길래 community.serializers에 있는거 한번 더 만듬
class ReviewUserCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','username',)

class CommunityCommentSerializer(serializers.ModelSerializer):
    user = ReviewUserCommentSerializer()
    
    class Meta:
        model = Comment
        fields = '__all__'

class ReviewListSerializer(serializers.ModelSerializer):
    review_comments = CommunityCommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='review_comments.count', read_only=True)
    user = ReviewUserCommentSerializer()
    
    class Meta:
        model = Review
        # fields = '__all__'
        fields = ('id', 'review_comments', 'comment_count', 'rating', 'likes', 'movie', 'user', 'title',)


class MovieListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ('id','poster_path',)
        # fields = '__all__'

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
    genres = GenreSerializer(many=True, read_only=True)
    keywords = KeywordSerializer(many=True, read_only=True)
    directors = PeopleSerializer(many=True, read_only=True)
    actors = PeopleSerializer(many=True, read_only=True)
    movie_reviews = ReviewListSerializer(many=True, read_only=True)
    # review에 달린 comments 갯수도 보내야함
    class Meta:
        model = Movie
        fields = ('id','title','runtime', 'release_date', 'likes', 'overview', 'original_title',
        'genres', 'keywords', 'directors', 'actors', 'movie_reviews','backdrop_path',)

class ProfileMovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title', 'original_title', 'poster_path',)


