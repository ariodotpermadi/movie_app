from django.core.management.base import BaseCommand
from django.forms import IntegerField
from movie_app import models
from movie_app.models import Movie
import json

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with open('movie_app/movies.json') as file:
            movies = json.load(file)
            for movie in movies:
                Movie.objects.create(
                    id=movie['id'],
                    name=movie['name'],
                    description=movie['description'],
                    imgPath=movie['imgPath'],                    
                    durations=int(movie['duration']),
                    genre=movie['genre'],
                    language=movie['language'],
                    mpaaRatingType=movie['mpaaRating']['type'],
                    mpaaRatingLabel=movie['mpaaRating']['label'],
                    userRating=int(movie['userRating'])
                )
        self.stdout.write(self.style.SUCCESS('Film Data success added'))
