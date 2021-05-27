from django.urls import path, include
from . import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from rest_framework.permissions import AllowAny
from rest_framework import routers, permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Movie Data API", # 타이틀
        default_version='m1', # 버전
        description="영화 관련 정보를 주는 API 입니다.", # 설명
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="qkdwlghks00@gmail.com"),
        license=openapi.License(name="SSAFY License"),
    ),
)


urlpatterns = [
    path('updateDB/', views.update_DB),
    # 영화정보 불러오기
    path('movie/', views.movie_list),
    path('movie/selectlike/',views.select_like_movie),
    path('movie/<int:movie_pk>/', views.movie_detail),
    # 좋아요 눌러져 있으면 취소
    path('movie/<int:movie_pk>/like/', views.movie_like),
    # 좋아요만 가능
    path('movie/<int:movie_pk>/likes/', views.movie_only_like),
    path('movie/<int:movie_pk>/hate/', views.movie_hate),
    path('search/<search_word>/', views.search),
    path('person/<name>/', views.search_person),
    path('movie/recommend/random/', views.recommend_random),
    path('movie/recommend/genre/most/', views.recommend_genre_most),
    path('movie/recommend/keyword/', views.recommend_keyword_most),
    path('movie/recommend/genre/', views.recommend_genre),
    
    # 비슷한 장르 추천
    path('movie/recommend/similargenre/<int:movie_pk>/',views.recommend_similar_genre),
    # 최신 인기순
    path('movie/recommend/new/',views.movie_new),
    # 평점순
    # path('movie/recommend/rating/',views.movie_rating),
    # 상영시간순
    path('movie/recommend/runtime/',views.movie_runtime),



    path('swagger/', schema_view.with_ui('swagger')),

]
