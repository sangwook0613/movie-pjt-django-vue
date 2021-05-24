from random import choice

from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.db.models import Max, query
from django.contrib.auth import get_user_model


from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import MovieSerializer, MovieListSerializer, PeopleSerializer
from .models import Genre, Movie, Keyword, Person
from .create_db import createDB


# 전체 영화 리스트
# @api_view(['GET', 'POST'])
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication]) # JWT가 유효한지 여부를 판단
@permission_classes([IsAuthenticated]) # 인증 여부를 확인
def movie_list(request):
    if request.method == 'GET':
        # 영화 전체 쿼리셋 가져오기
        movies = get_list_or_404(Movie)
        # 시리얼라이징
        serializer = MovieListSerializer(movies, many=True)
        #반환
        return Response(serializer.data)
    '''
    elif request.method == 'POST':
        serializer = MovieListSerializer(data=request.data)
        # 유효성 검사를 진행한다. -> 만약 유효하지 않은 데이터가 들어온다면 400 Bad Request 에러를 발생
        if serializer.is_valid(raise_exception=True):
            # 저장한다.
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    '''
# 단일 영화 페이지
# @api_view(['GET', 'PUT', 'DELETE'])
# PUT, DELETE는 admin페이지에서 해서 주석처리
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def movie_detail(request, movie_pk):
    # pk에 해당하는 영화 하나
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        # 시리얼라이징
        serializer = MovieSerializer(movie)
        # 반환
        return Response(serializer.data)
    '''
    elif request.method == 'DELETE':
        #1. 삭제한다.
        movie.delete()
        data = {
            'delete': f'데이터 {movie_pk}번이 정상적으로 삭제되었습니다.'
        }
        #2. 어떤 데이터가 삭제 되었는지 알 수 있는 정보를 상태 코드와 함께 응답한다.
        return Response(data, status=status.HTTP_204_NO_CONTENT)
        
    # 수정
    elif request.method == 'PUT':
        serializer = MovieDetailSerializer(Movie, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    '''

@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def movie_like(request, movie_pk):
    if request.method == 'POST':
        movie = get_object_or_404(Movie, pk=movie_pk)
        # 좋아요 눌려있으면
        if movie.likes.filter(pk=request.user.pk).exists():
            # 취소
            movie.likes.remove(request.user)
        #아니면
        else:
            # 좋아요
            movie.likes.add(request.user)

        # 시리얼 라이징
        serializer = MovieSerializer(movie)
        # 반환
        return Response(serializer.data)



@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def movie_likes(request, movie_pk):
    if request.method == 'POST':
        movie = get_object_or_404(Movie, pk=movie_pk)
        # 좋아요 눌려있으면
        if movie.likes.filter(pk=request.user.pk).exists():
            pass
        #아니면
        else:
            # 좋아요
            movie.likes.add(request.user)

        # 시리얼 라이징
        serializer = MovieSerializer(movie)
        # 반환
        return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def movie_hate(request, movie_pk):
    if request.method =='POST':
        movie = get_object_or_404(Movie, pk=movie_pk)
        if movie.hate_movies.filter(pk=request.user.pk).exists():
            movie.hate_movies.remove(request.user)
        else:
            movie.hate_movies.add(request.user)

        serializer = MovieSerializer(movie)
        return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def search(request, search_word):
    movies = Movie.objects.all()
    if request.method == 'GET':
        search_title = movies.filter(title__contains=search_word)
        search_overview = movies.filter(overview__contains=search_word)
        search_original_title = movies.filter(original_title__contains=search_word)
        result = search_title.union(search_overview, all=False)
        result = result.union(search_original_title, all=False)

        if result:
            serializer = MovieListSerializer(result, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def search_person(request, name):
    people = Person.objects.all()
    if request.method == 'GET':
        search_name = people.filter(name__contains=name)
        search_eng_name = people.filter(eng_name__contains=name)
        result = search_name.union(search_eng_name, all=True)

        if result:
            serializer = PeopleSerializer(result, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def select_like_movie(request):
    # movies = Movie.objects.order_by('id')[:15]
    movies = Movie.objects.order_by('?')[:15]
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def recommend_random(request):
    # 랜덤 정렬하고 앞에서 15개
    movies = Movie.objects.order_by('?')[:15]
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)



# most 장르 추천
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def recommend_genre_most(request):
    # 내가 좋아요 한 영화들 가져온다.
    movies = request.user.like_movies.all()
    # 장르 카운팅할 dict
    genre_cnt = {}
    # 영화들 반복하면서
    for movie in movies:
        # 장르들을 가져온다.
        genres = movie.genres.all()
        # 장르를 돌면서 카운팅
        for genre in genres:
            if genre_cnt.get(genre):
                genre_cnt[genre] += 1
            else:
                genre_cnt[genre] = 1
    
    # 최댓값 가진 장르 찾기
    most_genre = 0
    most_cnt = 0
    for key, value in sorted(genre_cnt.items(), key=lambda item: item[1], reverse=True):
        if not most_genre:
            most_genre = key
            break

    # 제일 좋아하는 장르의 id
    most_genre_id = most_genre.pk

    # 내가 이미 좋아요 누른 장르들 제외하고 전체 영화 쿼리셋 생성
    exclude_movies = Movie.objects.exclude(pk__in=[movie.pk for movie in movies]).order_by('-vote_count')
    count = 0
    recommend_movies = []
    # 15개 추출할때까지 반복
    for ex_movie in exclude_movies:
        if count >= 15:
            break
        ex_movie_genres = ex_movie.genres.all()
        for ex_movie_genre in ex_movie_genres:
            # 같은 장르 id가 있으면 추가해준다
            if ex_movie_genre.id == most_genre_id:
                recommend_movies.append(ex_movie)
                count += 1
                break

    # 시리얼라이징 후 반환
    serializer = MovieListSerializer(recommend_movies, many=True)
    return Response(serializer.data)


# 장르별로 추천
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def recommend_genre(request):
    # 내가 좋아요 한 영화들 가져온다.
    movies = request.user.like_movies.all()
    genre_cnt = {}
    for movie in movies:
        genres = movie.genres.all()
        for genre in genres:
            if genre_cnt.get(genre):
                genre_cnt[genre] += 1
            else:
                genre_cnt[genre] = 1
    
    # 2,3,4 번째 좋아하는 장르 찾기
    most_genre = most_genre2 = most_genre3 = most_genre4 = 0
    for key, value in sorted(genre_cnt.items(), key=lambda item: item[1], reverse=True):
        if not most_genre:
            most_genre = key
        elif not most_genre2 and most_genre2 != most_genre:
            most_genre2 = key
        elif not most_genre3 and most_genre3 != most_genre2:
            most_genre3 = key
        elif not most_genre4 and most_genre4 != most_genre3:
            most_genre4 = key
            break
        
    # 제일 좋아하는 장르의 id
    if most_genre:
        most_genre_id1 = most_genre.pk
    if most_genre2:
        most_genre_id2 = most_genre2.pk
    if most_genre3:
        most_genre_id3 = most_genre3.pk
    if most_genre3:
        most_genre_id4 = most_genre4.pk

    exclude_movies = Movie.objects.exclude(pk__in=[movie.pk for movie in movies]).order_by('-vote_count')
    count = 0
    recommend_movies1 = []
    # 15개 추출할때까지 반복
    for ex_movie in exclude_movies:
        if count >= 15:
            break
        ex_movie_genres = ex_movie.genres.all()
        for ex_movie_genre in ex_movie_genres:
            # 같은 장르 id가 있으면 추가해준다
            if ex_movie_genre.id == most_genre_id1:
                recommend_movies1.append(ex_movie)
                count += 1
                break

    # 내가 이미 좋아요 누른 장르들 제외하고 전체 영화 쿼리셋 생성
    exclude_movies = Movie.objects.exclude(pk__in=[movie.pk for movie in movies]).order_by('-vote_count')
    recommend_movies = set()

    # 5개씩 추출
    for ex_movie in exclude_movies:
        if len(recommend_movies) < 5:
            ex_movie_genres = ex_movie.genres.all()
            for ex_movie_genre in ex_movie_genres:
                # 같은 장르 id가 있으면 추가해준다
                if ex_movie_genre.id == most_genre_id2 and (ex_movie not in recommend_movies1):
                    recommend_movies.add(ex_movie)

        elif len(recommend_movies) < 10:
            ex_movie_genres = ex_movie.genres.all()
            for ex_movie_genre in ex_movie_genres:
                if ex_movie_genre.id == most_genre_id3 and (ex_movie not in recommend_movies1):
                    recommend_movies.add(ex_movie)

        elif len(recommend_movies) < 15:
            ex_movie_genres = ex_movie.genres.all()
            for ex_movie_genre in ex_movie_genres:
                if ex_movie_genre.id == most_genre_id4 and (ex_movie not in recommend_movies1):
                    recommend_movies.add(ex_movie)

        else:
            break
        
    # 시리얼라이징 후 반환
    serializer = MovieListSerializer(recommend_movies, many=True)
    return Response(serializer.data)


import csv
import datetime
from django.http import HttpResponse


#### 추후 작업 필요 ####

# 클러스터링을 활용하여 유저 맞춤 추천
@api_view(['GET'])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
def recommend_likes(request):
    pass
    # print(Movie.objects.get(id=50).release_date)
    # print(type(Movie.objects.get(id=50).release_date))
    # print(datetime.date.today())
    # print(type(datetime.date.today()))
    # print(datetime.date.today() > '2019-01-01')
    # print(datetime.date.today() > Movie.objects.get(id=1).release_date)

    # cnt = 0
    # for keyword in Keyword.objects.all():
    #     if keyword.keyword_count == 1:
    #         cnt += 1
    # print(cnt, len(Keyword.objects.all()))
    
    # cut_num = 1
    # for keyword in Keyword.objects.all():
    #     if keyword.keyword_count == cut_num:
    #         keyword.delete()
    
    # print(len(Keyword.objects.all()))



def create_csv(request):
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)

    # 컬럼명 생성
    column_names = ['id']
    for genre in Genre.objects.all():
        column_names.append(f'g_{genre.id}')

    for keyword in Keyword.objects.all():
        column_names.append(f'k_{keyword.id}')
    print(len(column_names))
    writer.writerow(column_names)

    # row데이터 추가
    for i in range(5):
        temp_row = []
        for j in range(len(column_names)):
            temp_row.append(j)
        writer.writerow(temp_row)
    

    response['Content-Disposition'] = 'attachment; filename="movie_data.csv"'
    return response
    



## DB 생성하기
def updateDB(request):
    createDB(request)