from django.shortcuts import render
from .models import Movie, Genre


def index(request):
    movies = Movie.objects.all()
    return render(request, 'app/index.html', {'movies': movies})

def detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'app/detail.html', {'movie': movie})

def genre(request, genre_id):
    genre = Genre.objects.get(id=genre_id)
    return render(request, 'app/genre.html', {'genre': genre})

