from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:movie_id>/', views.detail, name='detail'),
    path('genre/<int:genre_id>/', views.genre, name='genre'),
]
