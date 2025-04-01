from rest_framework.response import Response
from rest_framework.decorators import api_view
from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer

@api_view(['GET','post'])  # Allow only GET requests
def movie_list(request):
    if request.method=='GET':
        movies=Movie.objects.all()
        serializer=MovieSerializer(movies,many=True)
        return Response(serializer.data)
    
    if request.method=='POST':  
        serializer=MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        else:
            return Response(serializer.errors)

@api_view(['GET','PUT','DELETE'])  # Allow only GET requests
def movie_detail(request, movie_id):
    if request.method=='GET':  # Retrieve a movie
        movie=Movie.objects.get(pk=movie_id)
        serializer=MovieSerializer(movie)
        return Response(serializer.data) 

    if request.method=='PUT':
        movie=Movie.objects.get(pk=movie_id)
        serializer=MovieSerializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
            
    if request.method=='DELETE':
        movie=Movie.objects.get(pk=movie_id)
        movie.delete()
        return Response(status=204)  # No content status code
        
     
    
    