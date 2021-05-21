from django.urls import path
from . import views

urlpatterns = [
    path('updateDB/',views.updateDB),
    path('movie/', views.movie_list),
    path('movie/<int:movie_pk>/', views.movie_detail),
    path('movie/<int:movie_pk>/like/', views.movie_like),
    path('movie/<int:movie_pk>/hate/', views.movie_hate),
    path('search/<search_word>/', views.search),
    path('person/<name>/', views.search_person),
    path('movie/recommend/random/', views.recommend_random),
    path('movie/recommend/genre/most/', views.recommend_genre_most),
    path('movie/recommend/genre/', views.recommend_genre),
]
