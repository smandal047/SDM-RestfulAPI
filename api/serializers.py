from rest_framework import serializers

from movies.models import Movies, MoviePoster


class MoviesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movies
        fields = ('popularity', 'director', 'genre', 'imdb_score', 'name')


class MoviePosterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MoviePoster
        fields = ('name', 'poster_url')
