from django.shortcuts import render
from .models import Still
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.response import Response
from .serializers import StillSerializer
from django.http import JsonResponse

def still_list(request, colorChoice):
    print(colorChoice)
    if colorChoice == 'ALL':
        print('still_list 진입')
        still_list = get_list_or_404(Still)
        print('still_list: ', still_list)
        serializer = StillSerializer(still_list, many=True)
        print('serializer.data : ', serializer.data)
    else:
        print('still_of_color 진입')
        still_of_color_list = get_list_or_404(Still, still_color=colorChoice)
        print('still_of_color_list: ', still_of_color_list)
        serializer = StillSerializer(still_of_color_list, many=True)
        print('serializer.data : ', serializer.data)
        # 만약 일치하는 데이터가 없다면 []가 반환된다.
    return JsonResponse(serializer.data, safe=False)