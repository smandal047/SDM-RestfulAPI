from django.db import models


# Create your models here.

class Movies(models.Model):
    """ Sample data item that needs to be stored
    TABLE 1
    "popularity": 83.0,
    "director": "Victor Fleming",
    "genre": [
      "Adventure",
      " Family",
      " Fantasy",
      " Musical"
    ],
    "imdb_score": 8.3,
    "name": "The Wizard of Oz",

    TABLE 2
    "poster_id": 1,
    "poster_url": "https://picsum.photos/id/1006/3000/2000"
    """

    popularity = models.DecimalField(decimal_places=2, max_digits=1000)
    director = models.CharField(max_length=120)
    genre = models.TextField()
    imdb_score = models.DecimalField(decimal_places=2, max_digits=1000)
    name = models.CharField(max_length=120)

    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "Movies"

    def __str__(self):
        return self.name


class MoviePoster(models.Model):
    name = models.ForeignKey(Movies, default=1, verbose_name="Movies", on_delete=models.SET_DEFAULT)
    poster_url = models.TextField(null=False)

    def __str__(self):
        return self.poster_url
