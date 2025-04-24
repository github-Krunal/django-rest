from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from watchlist_app.api.views import movie_list,movie_detail
from watchlist_app.api.views import (WatchListAv,WatchDetailAv,StreamPlatformAv,
                                     StreamPlatformDetailAv,ReviewList,ReviewDetail,ReviewCreate,StreamPlatformVS)

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    path("list/",WatchListAv.as_view(),name='movie-list'),  # Include watchlist_app URLs
    path("<int:movie_id>/",WatchDetailAv.as_view(),name="movie-detail"),  # Include watchlist_app URLs
    
    path('', include(router.urls)),
    
    # path("stream/",StreamPlatformAv.as_view(),name="stream-list"),  # Include watchlist_app URLs
    # path("stream/<int:stream_id>/",StreamPlatformDetailAv.as_view(),name="stream-details"),  # Include watchlist_app URLs
    
    # path('review/',ReviewList.as_view(),name="review-list"),
    # path('review/<int:pk>/',ReviewDetail.as_view(),name="review-detail")
    
    path('stream/<int:pk>/review-create',ReviewCreate.as_view(),name="review-create"),
    path('stream/<int:pk>/review',ReviewList.as_view(),name="review-list"),
    path('stream/review/<int:pk>',ReviewDetail.as_view(),name="review-detail")
    
]
