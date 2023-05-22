from django.shortcuts import render
from .models import Still, Movie
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.response import Response
from .serializers import StillSerializer, MovieSerializer
from django.http import JsonResponse

def still_list(request, colorChoice):
    print(colorChoice)
    if colorChoice == 'ALL':
        print('still_list 진입')
        still_list = Still.objects.all()
        print('still_list: ', still_list)
        serializer = StillSerializer(still_list, many=True)
        print('serializer.data : ', serializer.data)
    else:
        print('still_of_color 진입')
        still_of_color_list = Still.objects.filter(still_color=colorChoice)
        print('still_of_color_list: ', still_of_color_list)
        serializer = StillSerializer(still_of_color_list, many=True)
        print('serializer.data : ', serializer.data)
        # 만약 일치하는 데이터가 없다면 []가 반환된다.
    return JsonResponse(serializer.data, safe=False)

def still_detail(request, stillId):
    print('still_detail 진입!!')
    still = Still.objects.get(id=stillId)
    still_serializer = StillSerializer(still)
    # 영화 Id 받아오기
    movieId = still_serializer.data['movie_id']
    print('movieId: ', movieId)
    movie = Movie.objects.filter(id=movieId)
    movie_serializer = MovieSerializer(movie, many=True)
    context = {
        'still': still_serializer.data,
        'movie': movie_serializer.data,
    }
    return JsonResponse(context)

def recommend_still(request, color):
    if color == 'RED':
        recommend_color = ['ORANGE', 'YELLOW']
    elif color == 'ORANGE':
        recommend_color = ['RED', 'YELLOW']
    elif color == 'YELLOW':
        recommend_color = ['ORANGE', 'GREEN']
    elif color == 'GREEN':
        recommend_color = ['YELLOW']
    elif color == 'BLUE':
        recommend_color = ['PURPLE']
    elif color == 'PINK':
        recommend_color = ['PURPLE']
    elif color == 'PURPLE':
        recommend_color = ['BLUE', 'PINK']
    elif color == 'WHITE':
        recommend_color = ['GREY']
    elif color == 'GREY':
        recommend_color = ['BLACK']
    else:
        recommend_color = ['GREY']
    print('recommend_still 진입', recommend_color)
    recommend_still_list = Still.objects.filter(still_color__in=recommend_color)
    print('recommend_still_list: ', recommend_still_list)
    serializer = StillSerializer(recommend_still_list, many=True)
    print('serializer.data : ', serializer.data)
    # 만약 일치하는 데이터가 없다면 []가 반환된다.
    return JsonResponse(serializer.data, safe=False)