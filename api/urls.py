from django.urls import include, path
from rest_framework import routers
from .views import MoviesViewSet, MoviePosterViewSet

router = routers.DefaultRouter()
router.register(r'movies', MoviesViewSet)
router.register(r'movie-poster', MoviePosterViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
