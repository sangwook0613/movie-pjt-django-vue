from rest_framework import serializers
from django.contrib.auth import get_user_model
from community.serializers import ReviewListSerializer, CommentListSerializer
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password')

class UpdateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'introduction')

class FollowerSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username',)


class UserProfileSerializer(serializers.ModelSerializer):
    # 팔로워 수, 팔로잉 수
    followers_count = serializers.IntegerField(source='followers.count', read_only=True)
    followings_count = serializers.IntegerField(source='followings.count', read_only=True)
    # 팔로워, 팔로잉
    followers = FollowerSerializer(many=True, read_only=True)
    followings = FollowerSerializer(many=True, read_only=True)
    # 작성한 리뷰, 작성한 댓글, 좋아요 한 리뷰
    # reviews = ReviewListSerializer(many=True, read_only=True)
    # comments = CommentListSerializer(many=True, read_only=True)
    # 좋아요 한 영화, 싫어요 한 영화
    class Meta:
        model = User
        fields = ('username', 'introduction', 'followers', 'followings','followers_count', 'followings_count', 'reviews',
         'comments', 'like_movies', 'hate_movies', 'like_reviews')