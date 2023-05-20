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

# pip install opencv-python


@api_view(['GET', 'POST'])
def post(request):
    # 이미지 파일이 있다면 컬러를 검사한다.
    if request.method == 'POST':
        print('★'*30)
        # 유저가 제출한 이미지를 가져온다
        image_file = request.FILES.get('still_image')

        '''
        still_color(대표 색상) 추출 로직
        '''
        # [1] (r, g, b)값 뽑아서 딕셔너리로 저장: 최댓값, 중간값, 최솟값을 키로 찾을 수 있도록
        ct = ColorThief("beige.jpg")
        r, g, b = ct.get_color(quality=1)
        rgb = {'r': r, 'g': g, 'b': b}
        still_color = 'WHITE'

        # [2] 최댓값, 중간값, 최솟값 찾기: rgb 딕셔너리의 키로 활용할 수 있도록 문자로 저장
        max, mid, min = '', '', ''
        if r >= g and r >= b:                       # r값이 제일 클 경우
            if g >= b:
                max, mid, min = 'r', 'g', 'b'
            else:
                max, mid, min = 'r', 'b', 'g'
        elif g >= r and g >= b:                     # g값이 가장 클 경우
            if r >= b:
                max, mid, min = 'g', 'r', 'b'
            else:
                max, mid, min = 'g', 'b', 'r'
        else:                                       # b값이 가장 클 경우
            if r >= g:
                max, mid, min = 'b', 'r', 'g'
            else:
                max, mid, min = 'b', 'g', 'r'

        # [3] 흰색, 회색, 검정색 or OTHERS
        if rgb[min] >= 200 and rgb[max] - rgb[min] <= 16:
            # [4] 흰색: 모든 값이 200 이상이고, 값 차이가 16 이내이면 하양
            still_color = 'WHITE'

        elif rgb[max] - rgb[min] <= 10:
            # [5] 흰색, 회색, 검정색: 색상끼리의 차이가 10이내이면 모노톤
            if rgb[min] >= 200:                     # 최솟값이 200 이상일 경우 <<하양>>
                still_color = 'WHITE'
            elif rgb[max] <= 64:                    # 최댓값이 64 이하일 경우 <<검정>>
                still_color = 'BLACK'
            else:                                   # 그 외는 모두 <<회색>>
                still_color = 'GREY'

        else:
            if max == 'r':
                # [6] 빨간 계열: 빨강, 주황, 노랑, 분홍, 보라
                if mid == 'g':                      # 빨강, 주황, 노랑
                    if rgb[mid] <= 64:              # <<빨강>>
                        still_color = 'RED'
                    elif rgb[mid] <= 191:           # <<주황>>
                        still_color = 'ORANGE'
                    else:                           # <<노랑>>
                        still_color = 'YELLOW'
                else:                               # 빨강, 분홍, 보라
                    if rgb[mid] <= 32:              # <<빨강>>
                        still_color = 'RED'
                    elif rgb[max] <= 128:           # <<보라>>
                        still_color = 'PURPLE'
                    else:                           # <<분홍>>
                        still_color = 'PINK'

            elif max == 'g':
                # [7] 초록 계열: 초록
                still_color = 'GREEN'

            else: 
                # [8] 파랑 계열: 파랑, 분홍, 보라
                if mid == 'r':                      # 파랑, 분홍, 보라
                    if rgb[mid] >= 191:             # <<분홍>>
                        still_color = 'PINK'
                    if rgb[max] - rgb[mid] <= 128:  # <<보라>>
                        still_color = 'PURPLE'
                    else:                           # <<파랑>>
                        still_color = 'BLUE'
                else:                               # <<파랑>>
                    still_color = 'BLUE'

        print('^' * 50)
        print('11')
        print('이 이미지를 작성한 user id : ', request.user.id)
        # 이미지 파일을 업로드하고 나머지 필드와 함께 직렬화할 수 있는 데이터 객체를 생성합니다.
        data = {
            'still_image': image_file,
            # **remaining_fields,
            'user': request.user.id,  # post 요청을 보낸 유저의 아이디로 설정합니다.
            'still_color': still_color,
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
            print('★'*30, '성공')
            return Response(serializer.data, status=201)
        print('♥︎'*30)
        print(serializer.errors)
        return Response(serializer.errors, status=400)

    return Response(status=200)
