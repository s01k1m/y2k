from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
import json
from .serializers import PostSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from stills.models import Movie

from colorthief import ColorThief
import matplotlib.pyplot as plt
import colorsys


@api_view(['GET', 'POST'])
def post(request):
    # 이미지 파일이 있다면 컬러를 검사한다.
    if request.method == 'POST':
        print('★'*30)
        # 유저가 제출한 이미지를 가져온다
        image_file = request.FILES.get('still_image')

        ct = ColorThief(image_file)
        dominant_color = ct.get_color(quality=1)
        print(dominant_color)
        print('^' * 50)
        print('11')
        print('이 이미지를 작성한 user id : ', request.user.id)
        # 이미지 파일을 업로드하고 나머지 필드와 함께 직렬화할 수 있는 데이터 객체를 생성합니다.
        data = {
            'still_image': image_file,
            # **remaining_fields,
            'user': request.user.id,  # post 요청을 보낸 유저의 아이디로 설정합니다.
            'still_color': 'RED',
            'movie_id': 1,
        }

        # 'user': request.user.id,  # post 요청을 보낸 유저의 아이디로 설정합니다.
        # TODO: 'movie_id': 1, 아직 로직 구현안됨
        print('22')
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            print('33')
            print(serializer)
            serializer.save()
            print('44')
            print('★'*30)
            return Response(serializer.data, status=201)
        print('♥︎'*30)
        print(serializer.errors)
        return Response(serializer.errors, status=400)

    return Response(status=200)
