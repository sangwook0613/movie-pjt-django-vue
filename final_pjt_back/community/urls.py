from django.urls import path
from . import views

urlpatterns = [
    path('review/',views.review_list),
    path('review/<int:review_pk>/',views.review_detail),
    path('review/<int:review_pk>/like/', views.review_like),
    path('review/<int:review_pk>/comments/',views.create_comment),

    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/',views.comment_detail),
]
