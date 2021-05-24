from rest_framework import serializers
from .models import Review, Comment
from django.db import models
from movies.serializers import MovieSerializer

class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('review',)

class CommunityCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'

class CommentListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'


class ReviewCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        # fields = ('user', 'id','title','content','rating')
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    review_comments = CommunityCommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='review_comments.count', read_only=True)
    # movie, comments
    movie = MovieSerializer()
    class Meta:
        model = Review
        # fields = '__all__'
        fields = ('id', 'title', 'content', 'created_at', 'updated_at', 
        'rating', 'likes', 'review_comments', 'comment_count', 'movie', 'user',)