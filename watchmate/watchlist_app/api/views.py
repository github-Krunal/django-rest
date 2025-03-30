from rest_framework.response import Response
from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer

def movie_list(request):
    movies=Movie.objects.all()
    serializer=MovieSerializer(movies)
    return Response(serializer.data)

def movie_detail(request, movie_id):
    movie=Movie.objects.get(pk=movie_id)
    serializer=MovieSerializer(movie)
    return Response(serializer.data) 
    
    