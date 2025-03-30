from rest_framework.response import Response
from rest_framework.decorators import api_view
from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer

@api_view(['GET'])  # Allow only GET requests
def movie_list(request):
    movies=Movie.objects.all()
    serializer=MovieSerializer(movies,many=True)
    return Response(serializer.data)

@api_view(['GET'])  # Allow only GET requests
def movie_detail(request, movie_id):
    movie=Movie.objects.get(pk=movie_id)
    serializer=MovieSerializer(movie)
    return Response(serializer.data) 
    
    