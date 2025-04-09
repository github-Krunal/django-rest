from rest_framework.response import Response
from rest_framework import status
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from watchlist_app.models import WatchList,SteramPlatform
from watchlist_app.api.serializers import WatchListSerializer,StreamPlatformSerializer


class StreamPlatformAv(APIView):
    
    def get(self, request):
        platform=SteramPlatform.objects.all()
        serializer=StreamPlatformSerializer(platform,many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer=StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class StreamPlatformDetailAv(APIView):
    
    def get(self, request, stream_id):
        try:
            movie=SteramPlatform.objects.get(pk=stream_id)
        except SteramPlatform.DoesNotExist:
            return Response({'Error':'Movie not found'},status=status.HTTP_404_NOT_FOUND)  # Return 404 status code for not found movie
            
        serializer=StreamPlatformSerializer(movie)
        return Response(serializer.data,status=status.HTTP_200_OK) 
    
    def put(self, request, stream_id):
        movie = SteramPlatform.objects.get(pk=stream_id)
        serializer=StreamPlatformSerializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, stream_id):
        movie=SteramPlatform.objects.get(pk=stream_id)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  # No content status code


class WatchListAv(APIView):
    
    def get(self, request):
        movies=WatchList.objects.all()
        serializer=WatchListSerializer(movies,many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer=WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        else:
            return Response(serializer.errors)
        
class WatchDetailAv(APIView):
    
    def get(self, request, movie_id):
        try:
            movie=WatchList.objects.get(pk=movie_id)
        except WatchList.DoesNotExist:
            return Response({'Error':'Movie not found'},status=status.HTTP_404_NOT_FOUND)  # Return 404 status code for not found movie
            
        serializer=WatchListSerializer(movie)
        return Response(serializer.data,status=status.HTTP_200_OK) 
    
    def put(self, request, movie_id):
        movie = WatchList.objects.get(pk=movie_id)
        serializer=WatchListSerializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, movie_id):
        movie=WatchList.objects.get(pk=movie_id)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  # No content status code


# @api_view(['GET','post'])  # Allow only GET requests
# def movie_list(request):
#     if request.method=='GET':
#         movies=Movie.objects.all()
#         serializer=MovieSerializer(movies,many=True)
#         return Response(serializer.data)
    
#     if request.method=='POST':  
#         serializer=MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data) 
#         else:
#             return Response(serializer.errors)

# @api_view(['GET','PUT','DELETE'])  # Allow only GET requests
# def movie_detail(request, movie_id):
#     if request.method=='GET':  # Retrieve a movie
        
#         try:
#             movie=Movie.objects.get(pk=movie_id)
#         except Movie.DoesNotExist:
#             return Response({'Error':'Movie not found'},status=status.HTTP_404_NOT_FOUND)  # Return 404 status code for not found movie
            
#         serializer=MovieSerializer(movie)
#         return Response(serializer.data,status=status.HTTP_200_OK) 

#     if request.method=='PUT':
#         movie=Movie.objects.get(pk=movie_id)
#         serializer=MovieSerializer(movie,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            
#     if request.method=='DELETE':
#         movie=Movie.objects.get(pk=movie_id)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)  # No content status code
        
     
    
    