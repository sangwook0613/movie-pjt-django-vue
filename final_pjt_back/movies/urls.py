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
]
