import json
from django.shortcuts import get_object_or_404, render
from movie_app.models import Movie
# Create your views here.


def movie_list(request):
    with open('movie_app/movies.json') as file:
        movies = json.load(file)
    return render(request, 'movie_list.html', {'movies': movies})


def details(request, id):
    movie = Movie.objects.get(pk=id)
    with open('movie_app/movies.json') as file:
        movies = json.load(file)
        for m in movies:
            if m['id'] == id:
                movie.imgPath = m['imgPath']
                break
    return render(request, 'movie_details.html', {'movie': movie})
