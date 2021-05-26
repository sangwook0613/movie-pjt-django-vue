from django.urls import path
from . import views

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
    path('movie/recommend/likes/', views.recommend_likes),
]
