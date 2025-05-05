from rest_framework.response import Response
from rest_framework import status
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from watchlist_app.models import WatchList,SteramPlatform,Review
from watchlist_app.api.serializers import WatchListSerializer,StreamPlatformSerializer,ReviewSerializer
# from rest_framework import mixins
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError


class StreamPlatformVS(viewsets.ReadOnlyModelViewSet):
      queryset = SteramPlatform.objects.all()
      serializer_class = StreamPlatformSerializer

# class StreamPlatformVS(viewsets.ViewSet):

#     def list(self, request):
#         queryset = SteramPlatform.objects.all()
#         serializer = StreamPlatformSerializer(queryset, many=True,context={'request': request})
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = SteramPlatform.objects.all()
#         watchlist = get_object_or_404(queryset, pk=pk)
#         serializer = StreamPlatformSerializer(watchlist)
#         return Response(serializer.data)

#     def create(self, request):
#         serializer = StreamPlatformSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
    
class ReviewCreate(generics.CreateAPIView):
    serializer_class=ReviewSerializer
    
    def get_queryset(self):
        return Review.objects.all()
    
    def perform_create(self,serializer):
        pk=self.kwargs.get('pk')
        movie=WatchList.objects.get(pk=pk)
        
        review_user=self.request.user
        review_queryset=Review.objects.filter(watchList=movie,review_user=review_user)
        if review_queryset.exists():
            raise ValidationError("you already review this")
        serializer.save(watchList=movie,review_user=review_user)
        
class ReviewList(generics.ListAPIView):
    # queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    
    def get_queryset(self):
        pk=self.kwargs['pk']
        return Review.objects.filter(watchList=pk)
    
class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer


# class ReviewDetail(mixins.RetrieveModelMixin,generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

# class ReviewList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


class StreamPlatformAv(APIView):
    
    def get(self, request):
        platform=SteramPlatform.objects.all()
        serializer=StreamPlatformSerializer(platform,many=True,context={'request': request})
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
        
     
    
    