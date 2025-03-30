from django.urls import path, include
from watchlist_app.api.views import movie_list,movie_detail

urlpatterns = [
    path("list/",movie_list,name='movie-list'),  # Include watchlist_app URLs
    path("<int:movie_id>/",movie_detail,name="movie-detail"),  # Include watchlist_app URLs
]
