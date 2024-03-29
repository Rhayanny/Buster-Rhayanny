from django.urls import path
from .views import MoviesView, MovieDetailView
from movies_orders.views import MovieOrderView


urlpatterns = [
    path("movies/", MoviesView.as_view()),
    path("movies/<int:movie_id>/", MovieDetailView.as_view()),
    path("movies/<int:movie_id>/orders/", MovieOrderView.as_view()),
]
