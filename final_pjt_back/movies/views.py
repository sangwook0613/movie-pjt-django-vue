import re
from django.db.models.query import QuerySet
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, get_list_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import MovieSerializer, MovieListSerializer, PeopleSerializer
from .models import Genre, Movie, Keyword, Person
from django.db.models import Q

from .create_db import createDB

from drf_yasg.utils import swagger_auto_schema

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

@swagger_auto_schema(methods=['post'], request_body=MovieSerializer)
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



@swagger_auto_schema(methods=['post'], request_body=MovieSerializer)
@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def movie_only_like(request, movie_pk):
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


@swagger_auto_schema(methods=['post'], request_body=MovieSerializer)
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
    # 영화 전체, 배우 + 감독 전체
    movies = Movie.objects.all()
    persons = Person.objects.all()

    if request.method == 'GET':
        # 결과값 담을 빈 쿼리셋 생성
        result = Movie.objects.none()
        search_movie = movies.filter(Q(title__contains=search_word) | Q(overview__contains=search_word) | Q(original_title__contains=search_word))
        result = result.union(search_movie, all=False)

        if result.count() >= 50:
            result = result.order_by('-vote_count')[:50]
            print(result)
            serializer = MovieListSerializer(result, many=True)
            return Response(serializer.data)


        # 전체 person에서 검색어 포함하는 이름 가지고 있는 사람들 필터링 (여기선 배우 + 감독)
        search_person = persons.filter(Q(name__contains=search_word) | Q(eng_name__contains=search_word))

        # 뽑은 사람들 전체 돌면서 같은 이름 포함하면 더하기
        for person in search_person:
            search_person = movies.filter(Q(actors__name__contains=person.name) | Q(directors__name__contains=person.name)).distinct()
            result = result.union(search_person, all=False)
        
        if result:
            serializer = MovieListSerializer(result[:50], many=True)
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
    movies = Movie.objects.order_by('-vote_count')
    genres = Genre.objects.all().order_by('?')
    # 20개 보여주기 위해 1개 넣고 시작 (장르 총 19개)
    different_genre_movies = [movies[2]]
    # for movie in movies:
    #     print(movie.genres.all())
    cnt = 0
    for genre in genres:
        for movie in movies:
            chk = False
            for movie_gen in movie.genres.all():
                if genre == movie_gen and movie not in different_genre_movies:
                    different_genre_movies.append(movie)
                    # print(genre)
                    chk = True
                    break
            if chk:
                break

    serializer = MovieListSerializer(different_genre_movies, many=True)
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




# 선호 keyword 관련 추천
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def recommend_keyword_most(request):
    # 내가 좋아요 한 영화들 가져온다.
    movies = request.user.like_movies.all()
    # 장르 카운팅할 dict
    keyword_cnt = {}
    # 영화들 반복하면서
    for movie in movies:
        # 장르들을 가져온다.
        keywords = movie.keywords.all()
        # 장르를 돌면서 카운팅
        for keyword in keywords:
            if keyword_cnt.get(keyword):
                keyword_cnt[keyword] += 1
            else:
                keyword_cnt[keyword] = 1
    
    # 최댓값 가진 장르 찾기
    most_keyword = 0
    for key, value in sorted(keyword_cnt.items(), key=lambda item: item[1], reverse=True):
        most_keyword = key
        break

    # 제일 좋아하는 장르의 id
    most_keyword_id = most_keyword.pk

    # 내가 이미 좋아요 누른 영화들 제외하고 전체 영화 쿼리셋 생성
    exclude_movies = Movie.objects.exclude(pk__in=[movie.pk for movie in movies]).order_by('vote_count')
    count = 0
    recommend_movies = []
    # 15개 추출할때까지 반복
    for ex_movie in exclude_movies:
        if count >= 15:
            break
        ex_movie_keywords = ex_movie.keywords.all()
        for ex_movie_keyword in ex_movie_keywords:
            # 같은 장르 id가 있으면 추가해준다
            if ex_movie_keyword.id == most_keyword_id:
                recommend_movies.append(ex_movie)
                count += 1
                break

    # 시리얼라이징 후 반환
    serializer = MovieListSerializer(recommend_movies, many=True)
    return Response(serializer.data)




# 선택한 영화와 비슷한 장르의 영화 추천
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def recommend_similar_genre(request, movie_pk):
    # 중복제거용 set
    result = set()
    # 현재 영화
    my_movie = Movie.objects.get(pk=movie_pk)
    # 현재 영화를 제외한 영화들
    movies = Movie.objects.exclude(pk=movie_pk)
    # 현재 영화가 가진 장르들
    genres = my_movie.genres.all()
    genre_length = len(genres)
    # 전체 영화 돌면서
    for movie in movies:
        cnt = 0
        # 영화의 장르들을 전체 돌면서
        movie_genres = movie.genres.all()
        # 장르가 몇번 나왔는지카운트
        for movie_genre in movie_genres:
            if movie_genre in genres:
                cnt += 1
            # 현재 영화와 장르가 모두 일치하거나 3개 이상 일치하면 추가
            if cnt >= 3 or cnt >= genre_length:
                result.add(movie)

        # 5개의 데이터만 리턴
        if len(result) >= 4:
            serializer = MovieListSerializer(result, many=True)
            return Response(serializer.data)
    # 5개 미만이면 그대로 리턴
    if result:
        serializer = MovieListSerializer(result, many=True)
        return Response(serializer.data)
    # 없으면 204
    return Response(status=status.HTTP_204_NO_CONTENT)


# 개봉순
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def movie_new(request):
    movies = Movie.objects.exclude(runtime=0).order_by('-release_date')[:20]
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


# 평점순
# @api_view(['GET'])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
# def movie_rating(request):
#     movies = Movie.objects.order_by('likes__count')[:20]
#     serializer = MovieListSerializer(movies, many=True)
#     return Response(serializer.data)


# 시간순
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def movie_runtime(request):
    movies = Movie.objects.exclude(runtime=0).order_by('runtime')[:20]
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


# DB 업데이트용
def update_DB(request):
    createDB(request)