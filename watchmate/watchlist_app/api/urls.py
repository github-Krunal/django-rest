from django.urls import path, include
# from watchlist_app.api.views import movie_list,movie_detail
from watchlist_app.api.views import MovieListAv,MovieDetailAv

urlpatterns = [
    path("list/",MovieListAv.as_view(),name='movie-list'),  # Include watchlist_app URLs
    path("<int:movie_id>/",MovieDetailAv.as_view(),name="movie-detail"),  # Include watchlist_app URLs
]
