from django.shortcuts import render,redirect
from django.http import JsonResponse
import json
import base64
from .serializers import DecodeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class APITest(APIView):
        # id, still_image, still_color, movie_id, user, like_users

    def post(self, request) :
        data = request.data
        print('#' * 30)
        print('request data: ', data)
        #serializer 직렬화
        serializer = DecodeSerializer(data=data, context={'user': data.get("user"),'still_image':data.get("images")})

        # 데이터 유효성 검사
        if serializer.is_valid():
            # DB에 저장
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
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
