from django.urls import path, include
# from watchlist_app.api.views import movie_list,movie_detail
from watchlist_app.api.views import WatchListAv,MovieDetailAv,StreamPlatformAv,StreamPlatformDetailAv

urlpatterns = [
    path("list/",WatchListAv.as_view(),name='movie-list'),  # Include watchlist_app URLs
    path("<int:movie_id>/",MovieDetailAv.as_view(),name="movie-detail"),  # Include watchlist_app URLs
    
    path("stream",StreamPlatformAv.as_view(),name="stream"),  # Include watchlist_app URLs
    path("stream/<int:stream_id>/",StreamPlatformDetailAv.as_view(),name="stream-details"),  # Include watchlist_app URLs
    
]
