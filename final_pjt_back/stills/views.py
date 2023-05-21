from django.shortcuts import render
from .models import Still
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.response import Response

def still_list(request):
    still_list = get_list_or_404(Still)
    print(still_list)
    return Response(status=200)

def still_of_color(request, colorChoice):
    print('still_of_color 진입')
    still_of_color_list = get_list_or_404(Still, still_color=colorChoice)
    print('still_of_color_list: ', still_of_color_list)
    return Response(status=200)