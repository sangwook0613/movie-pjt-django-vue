from pprint import pprint
from bs4 import BeautifulSoup
import requests
from random import choice

from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.db.models import Max, query

from decouple import config

from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import MovieSerializer, MovieListSerializer, PeopleSerializer
from .models import Genre, Movie, Keyword, Person

from django.contrib.auth import get_user_model

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
        if movie.like_movies.filter(pk=request.user.pk).exists():
            # 취소
            movie.like_movies.remove(request.user)
        #아니면
        else:
            # 좋아요
            movie.like_movies.add(request.user)

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
        result = search_title.union(search_overview, all=True)

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
    if most_genre2:
        most_genre_id2 = most_genre2.pk
    if most_genre3:
        most_genre_id3 = most_genre3.pk
    if most_genre3:
        most_genre_id4 = most_genre4.pk

    # 내가 이미 좋아요 누른 장르들 제외하고 전체 영화 쿼리셋 생성
    exclude_movies = Movie.objects.exclude(pk__in=[movie.pk for movie in movies]).order_by('-vote_count')
    recommend_movies = set()

    # 5개씩 추출
    for ex_movie in exclude_movies:
        if len(recommend_movies) < 5:
            ex_movie_genres = ex_movie.genres.all()
            for ex_movie_genre in ex_movie_genres:
                # 같은 장르 id가 있으면 추가해준다
                if ex_movie_genre.id == most_genre_id2:
                    recommend_movies.add(ex_movie)
                    
        elif len(recommend_movies) < 10:
            ex_movie_genres = ex_movie.genres.all()
            for ex_movie_genre in ex_movie_genres:
                if ex_movie_genre.id == most_genre_id3:
                    recommend_movies.add(ex_movie)
                    
        elif len(recommend_movies) < 15:
            ex_movie_genres = ex_movie.genres.all()
            for ex_movie_genre in ex_movie_genres:
                if ex_movie_genre.id == most_genre_id4:
                    recommend_movies.add(ex_movie)
        else:
            break

    # 시리얼라이징 후 반환
    serializer = MovieListSerializer(recommend_movies, many=True)
    return Response(serializer.data)















NAVER_PAPAGO_DETECT_URL = 'https://openapi.naver.com/v1/papago/detectLangs'
NAVER_PAPAGO_TRANSLATE_URL = 'https://openapi.naver.com/v1/papago/n2mt'
MOVIE_API_KEY = config('MOVIE_API_KEY')
X_Naver_Client_Id = config('X_Naver_Client_Id')
X_Naver_Client_Secret = config('X_Naver_Client_Secret')
headers = {'X-Naver-Client-Id': X_Naver_Client_Id, 'X-Naver-Client-Secret': X_Naver_Client_Secret, 
                'Content-Type': 'application/x-www-form-urlencoded','charset':'utf-8'}
MOVIE_POPULAR_URL = f'https://api.themoviedb.org/3/movie/popular?api_key={MOVIE_API_KEY}&language=ko-KR&region=KR'
GENRE_URL = f'https://api.themoviedb.org/3/genre/movie/list?api_key={MOVIE_API_KEY}&language=ko-KR'

def updateDB(request):
    page = 1
    while page <= 5:
        MOVIE_URL = f'{MOVIE_POPULAR_URL}&page={page}'
        # 전체 장르 테이블 만들때 사용
        request_movies = requests.get(MOVIE_URL).json()
        request_genres = requests.get(GENRE_URL).json()
        genres = request_genres.get('genres')
        movies = request_movies.get('results')
        for genre in genres:
            genre_id = genre.get('id')
            genre_name = genre.get('name')
            genre_data = Genre(id=genre_id, name=genre_name)
            genre_data.save()
        
        for movie in movies:
            movie_id = movie.get('id')
            MOVIE_DETAIL_URL = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={MOVIE_API_KEY}&language=ko-KR'
            movie_detail = requests.get(MOVIE_DETAIL_URL).json()
            movie_title = movie.get('title')
            movie_original_title = movie.get('original_title')
            movie_overview = movie.get('overview')
            movie_poster_path = movie.get('poster_path')
            movie_release_date = movie.get('release_date')
            movie_backdrop_path = movie.get('backdrop_path')
            movie_genres = movie.get('genre_ids')
            movie_runtime = movie_detail.get('runtime')
            vote_average = movie.get('vote_average')
            vote_count = movie.get('vote_count')
            movie_data = Movie(title=movie_title, original_title=movie_original_title, overview=movie_overview,
                poster_path=f'https://image.tmdb.org/t/p/original{movie_poster_path}', runtime=movie_runtime,
                backdrop_path=f'https://image.tmdb.org/t/p/original{movie_backdrop_path}', release_date=movie_release_date,
                vote_average=vote_average, vote_count=vote_count)

            # 영화 제목으로 중복 체크
            if not Movie.objects.filter(title=movie_title).exists():
                movie_data.save()
                # 해당 영화 장르 M:N 테이블에 추가
                for g in movie_genres:
                    movie_data.genres.add(g)
            else:
                continue

            # CREDIT에서 people 정보
            MOVIE_CREDIT_URL = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={MOVIE_API_KEY}&language=ko-KR'
            movie_credit = requests.get(MOVIE_CREDIT_URL).json()
            cast = movie_credit.get('cast')
            crew = movie_credit.get('crew')
            cnt_actor = cnt_director = 0
            
            # 배우
            for people in cast:
                if people.get('profile_path') and people.get('known_for_department') == 'Acting':
                    # 10개만 추출
                    if cnt_actor == 10:
                        continue
                    actor_id = people.get('id')
                    actor_gender = people.get('gender')
                    actor_name = people.get('name')
                    actor_eng_name = people.get('original_name')
                    actor_profile_path = people.get('profile_path')
                    # Actor id에 해당하는 actor detail로 요청
                    ACTOR_DETAIL_URL = f'https://api.themoviedb.org/3/person/{actor_id}?api_key={MOVIE_API_KEY}&language=ko-KR'
                    actor_detail = requests.get(ACTOR_DETAIL_URL).json()
                    names = actor_detail.get('also_known_as')
                    for name in names:
                        # PAPAGO 언어 감지 결과 한글이면
                        NAVER_LANGEAGE_URL = f'{NAVER_PAPAGO_DETECT_URL}?query={name}'
                        # 파파고 요청 : post + header 필요
                        test_result_language = requests.post(NAVER_LANGEAGE_URL,headers=headers).json()
                        if test_result_language.get('langCode') == 'ko':
                            # actor_name = 한글 이름으로 교체
                            actor_name = name
                            break

                    # Actor 테이블에 중복검사
                    if not Person.objects.filter(id=actor_id).exists():
                        # 테이블에 없는 배우면 추가
                        people_data = Person(id=actor_id, gender=actor_gender, name=actor_name, 
                            eng_name=actor_eng_name, profile_path=f'https://image.tmdb.org/t/p/original{actor_profile_path}',
                            job='Actor')
                        people_data.save()

                    # 해당 영화 배우들 M:N 테이블에 추가
                    movie_data.actors.add(actor_id)
                    cnt_actor += 1
                    
            # 감독
            for people in crew:
                # 감독 = 1명
                if cnt_director == 1:
                        break
                if people.get('job') == 'Director':
                    director_id = people.get('id')
                    director_gender = people.get('gender')
                    director_name = people.get('name')
                    director_eng_name = people.get('original_name')
                    director_profile_path = people.get('profile_path')

                    DIRECTOR_DETAIL_URL = f'https://api.themoviedb.org/3/person/{director_id}?api_key={MOVIE_API_KEY}&language=ko-KR'
                    director_detail = requests.get(DIRECTOR_DETAIL_URL).json()
                    names = director_detail.get('also_known_as')
                    for name in names:
                        # PAPAGO 언어 감지 결과 한글이면
                        NAVER_LANGEAGE_URL = f'{NAVER_PAPAGO_DETECT_URL}?query={name}'
                        # 파파고 요청 : post + header 필요
                        test_result_language = requests.post(NAVER_LANGEAGE_URL,headers=headers).json()
                        if test_result_language.get('langCode') == 'ko':
                            # director_name = 한글 이름으로 교체
                            director_name = name
                            break

                    # Director 테이블에 중복검사
                    if not Person.objects.filter(id=director_id).exists():
                        # 테이블에 없는 감독이면 추가         
                        director_data = Person(id=director_id, gender=director_gender, name=director_name, 
                            eng_name=director_eng_name, profile_path=f'https://image.tmdb.org/t/p/original{director_profile_path}',
                            job='Director')
                        director_data.save()
                    
                    # 해당 영화 배우들 M:N 테이블에 추가
                    movie_data.directors.add(director_id)
                    cnt_director += 1
            
            MOVIE_KEYWORD_URL = f'https://api.themoviedb.org/3/movie/{movie_id}/keywords?api_key={MOVIE_API_KEY}'
            movie_keywords = requests.get(MOVIE_KEYWORD_URL).json()
            keywords = movie_keywords.get('keywords')
            for keyword in keywords:
                keyword_id = keyword.get('id')
                keyword_eng_name = keyword.get('name')
                # 키워드 없으면 추가
                if not Keyword.objects.filter(id=keyword_id).exists():
                    keyword_data = Keyword(id=keyword_id, keyword_eng_name=keyword_eng_name,)
                    keyword_data.save()

                    # 파파고 번역기
                #     data = {
                #         'text' : keyword_eng_name,
                #         'source': 'en',
                #         'target' : 'ko',
                #     }
                #     translate_result = requests.post(NAVER_PAPAGO_TRANSLATE_URL, headers=headers, data=data).json()
                #     keyword_name = translate_result.get('message').get('result').get('translatedText')
                    
                #     # 저장
                #     keyword_data = Keyword(id=keyword_id, keyword_name=keyword_name, keyword_eng_name=keyword_eng_name,)
                #     keyword_data.save()
                else:
                    keyword_data = Keyword.objects.get(id=keyword_id)
                    keyword_data.keyword_count = keyword_data.keyword_count + 1
                    keyword_data.save()

                # movie:keyword M:N 관계에 id 추가
                movie_data.keywords.add(keyword_id)

        page += 1


