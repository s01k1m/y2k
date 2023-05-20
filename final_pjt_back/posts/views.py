from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
import json
from .serializers import StillSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from stills.models import Movie


@api_view(['GET', 'POST'])
def post(request):
    if request.method == 'POST':
        print('POST 요청')
        data = request.FILES
        print(request.data)
        serializer = StillSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            print('♥︎☀︎★☆' * 30)
            data = request.FILES
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # serializer 직렬화
        ###################################
        # 컬러를 뽑는 함수 또는 로직을 추가해야합니다.
        color = 'RED'
        # m = Movie.objects.get(pk=1)
        u = get_user_model()
        uu = u.objects.get(pk=1)

        # serializer = StillSerializer(request.POST, request.FILES)
        # print(serializer)

    # # # 데이터 유효성 검사
    # if serializer.is_valid():
    #     # DB에 저장
    #     print('serializer.is valid 성공')
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)

    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # if request.method == 'POST':
    #     serializer = StillSerializer(data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save(user=request.user)
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.data , status=status.HTTP_201_CREATED)
    return Response(status=400)

    # if request.method == "POST":

    #     data = json.loads(request.body)
    #     # username = data['username']
    #     # password = data['password']

    #     img_string = request.data['img_base64'] # POST요청을 통해 받은 base64정보
    #     imgdata = base64.b64decode(img_string) # 디코딩

    #     filename = f'temp_image_{request.user}.jpg' # DB에 저장하지 않고 사용한다음 지우기 위해
    #     with open(filename, 'wb') as f:
    #         f.write(imgdata)				# 디코딩한 이미지를 사용하기 위해 잠시 저장
    #     #### 이미지를 사용하는 코드 #####
    #         os.remove(filename)    				# 이미지를 사용한 후 삭제
    #         return Response({'result' : result})

    #     # if username and password:
    #     #     response = f"Welcome {username}"
    #     #     return JsonResponse({"msg":response}, status=201)

    #     # else:
    #     #     response = "username or password is empty"
    #     #     return JsonResponse({"err":response}, status=400)

    # return render(request, 'submit-form.html')
