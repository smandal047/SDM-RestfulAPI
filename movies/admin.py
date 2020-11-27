from django.contrib import admin

# Register your models here.
from .models import Movies, MoviePoster

"""every app needs to be registered at the admin"""
admin.site.register(Movies)
admin.site.register(MoviePoster)
