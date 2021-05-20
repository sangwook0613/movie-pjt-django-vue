from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password')

class AllUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    # 팔로워 수, 팔로잉 수
    followers_count = serializers.IntegerField(source='followers.count', read_only=True)
    followings_count = serializers.IntegerField(source='followings.count', read_only=True)
    # 작성한 리뷰, 작성한 댓글, 좋아요 한 리뷰
    # reviews = 
    # comments = 
    # like_reviews = 
    # 좋아요 한 영화, 싫어요 한 영화
    # like_movies
    # hate_movies
    class Meta:
        model = User
        # fields = ('username', 'introduction', 'followers', 'followings', 'reviews',)
        fields = ('username', 'introduction', 'followers_count', 'followings_count')