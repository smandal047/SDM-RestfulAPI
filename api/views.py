from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, filters
from rest_framework.permissions import DjangoModelPermissions
from rest_framework import generics

from .serializers import MoviesSerializer, MoviePosterSerializer
from movies.models import Movies, MoviePoster


class MoviesViewSet(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissions]

    queryset = Movies.objects.all().order_by('name')
    serializer_class = MoviesSerializer


class MoviePosterViewSet(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissions]

    queryset = MoviePoster.objects.all().order_by('name')
    serializer_class = MoviePosterSerializer
