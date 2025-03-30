# from django.shortcuts import render
# from watchlist_app.models import Movie
# from django.http import JsonResponse

# def movie_list(request):
#     movies=Movie.objects.all()
#     print(list(movies.values()))
#     data ={
#         'movies':list(movies.values())
#     }
#     return JsonResponse(data)

# def movie_detail(request, movie_id):
#     movie=Movie.objects.get(pk=movie_id)
#     data={
#         "name": movie.name,
#         "description": movie.description,
#         "active": movie.active
#     }
#     print(movie)
#     return JsonResponse(data)