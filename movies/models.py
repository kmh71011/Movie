import datetime

from django.db import models
from django.utils import timezone


class Movie(models.Model):
    movie_title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="reviewBoard/images", blank=True)
    date = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.movie_title


class Information(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    actors = models.CharField(max_length=200)
    story = models.CharField(max_length=2000)


    def __str__(self):
        return self.actors
