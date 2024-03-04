from django.db import models

# Create your models here.

class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    imgPath = models.ImageField(upload_to='movie_images/')
    durations = models.IntegerField()
    genre = models.TextField()
    language = models.CharField(max_length=255)
    mpaaRatingType = models.CharField(max_length=255)
    mpaaRatingLabel = models.CharField(max_length=255)
    userRating = models.IntegerField()

    def __str__(self):
        return self.name