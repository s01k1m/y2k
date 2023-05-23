from django.shortcuts import render
from .models import Still, Movie
from django.shortcuts import get_list_or_404, get_object_or_404
from django.http import JsonResponse
from rest_framework.response import Response
from .serializers import StillSerializer, MovieSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from accounts.models import User

'''
Home 에서 컬러별, all로 still 이미지 가져오는 API : 
1. 색깔을 지정하면 그 색깔로 저장된 스틸을 반환합니다.
2. ALL을 지정하면 서버에 저장된 모든 스틸을 반환합니다.
'''

def still_list(request, colorChoice):
    if colorChoice == 'ALL':
        still_list = Still.objects.all()
        serializer = StillSerializer(still_list, many=True)
    else:
        still_of_color_list = Still.objects.filter(still_color=colorChoice)
        serializer = StillSerializer(still_of_color_list, many=True)
        # 만약 일치하는 데이터가 없다면 []가 반환된다.
    return JsonResponse(serializer.data, safe=False)


'''
Home에서 Search용 API :
1. 영화를 검색합니다.
2. 제목에 해당 단어가 들어간 모든 영화를 찾고
3. 그 영화로 작성된 스틸을 모두 반환합니다.
'''

@api_view(['GET'])
def searchMovie(request, search_query):
    #  movie_title 필드를 대소문자를 구분하지 않고 검색어 search_query를 포함하는 경우에 해당하는 무비 데이터를 가져온다.
    # [1] : 쿼리(검색어)가 영화 타이틀과 일치하는 것을 조회한다.
    movies = Movie.objects.filter(movie_title__icontains=search_query)

    serializer = MovieSerializer(movies, many=True) # 쿼리셋으로 영화를 가져오기 성공
    '''
    [{"id":16,"movie_id":603692,"movie_title":"존 윅 4","overview":"죽을 위기에서 살아난 존 윅은 최고 회의를 쓰러트릴 방법을 찾아낸다. 비로소 완전한 자유의 희망을 보지만, 빌런 그라몽 후작과 전 세계의 최강 연합은 존 윅의 오랜 친구까지 적으로 만들어 버리고, 새로운 위기에 놓인 존 윅은 최후의 반격을 준비하는데...","movie_released_date":"2023-03-22","genre":"['액션', '스릴러', '범죄']"},{"id":116,"movie_id":458156,"movie_title":"존 윅 3: 파라벨룸","overview":"사랑하는 아내와 반려견이 죽은 후 복수를 위해 돌아온 전설의 킬러, 존 윅은 성역 콘티넨탈 호텔에서는 살인하면 안 된다는 룰을 깨면서 전세계 킬러들의 표적이 된다. 전편에서 존 윅이 국제암살자연맹에서 파문당한 직후 1시간 동안 도망갈 시간을 내어 준 윈스턴은 최고회의로부터 그를 도왔다는 이유로 자리에서 물러날 것을 요구받는다. 현상금이 1400만달러로 불어난 존 윅은 옛 동료이자 현재 카사블랑카 콘티넨탈 호텔의 지점장인 소피아에게 도움을 청한다.","movie_released_date":"2019-05-15","genre":"['액션', '스릴러', '범죄']"},{"id":151,"movie_id":324552,"movie_title":"존 윅: 리로드","overview":"업계 최고의 레전드 킬러 존 윅은 과거를 뒤로 한 채 평화로운 삶을 꿈꾸며 은퇴를 선언하지만, 과거 자신의 목숨을 구해 줬던 옛 동료 산티노와의 피로 맺은 암살자들의 룰에 발목을 잡히고 만다. 피의 맹세에 대한 선택권 없이 산티노의 청을 들어줘야만 하는 존 윅은 산티노의 지시대로 로마로 향한다. 국제 암살자 연합의 최고 자리를 탈취하기 위해 자신의 친누나를 대신 암살하라는 산티노의 계획으로 인해 존 윅은 위험에 빠지게 되고, 무려 700만 달러의 현상금에 눈이 먼 전 세계의 암살자들의 총구는 그를 향하는데...","movie_released_date":"2017-02-08","genre":"['액션', '스릴러', '범죄']"},{"id":262,"movie_id":245891,"movie_title":"존 윅","overview":"전설이라 불리던 킬러 존 윅은 사랑하는 여인을 만나 결혼을 하면서 범죄의 세계에서 은퇴한다. 행복도 잠시, 투병 끝에 부인이 세상을 떠나고 그의 앞으로 부인이 죽기 전에 보낸 강아지 한 마리가 선물로 배달된다. 어느 날 그의 차를 탐낸 러시아 마피아의 일원 요세프가 존 윅을 폭행하고 애완견 데이지마저 죽여버리는 일이 벌어진다. 그런데 요세프는 과거 존 윅을 고용한 적 있는 러시아 마피아 보스 비고의 아들이다. 마지막 남은 애완견마저 잃은 존 윅은 이제 그만의 방식으로 복수를 시작하는데...","movie_released_date":"2014-10-22","genre":"['액션', '스릴러']"},{"id":1108,"movie_id":49529,"movie_title":"존 카터: 바숨 전쟁의 서막","overview":"신비의 행성, 바숨 이 곳은 외계 종족간의 계속된 전쟁으로 서서히 파괴되고 있다. 시공간 이동을 통해 우연히 이곳에 오게 된 존 카터(테일러 키취)는 상상조차 할 수 없었던 특별한 능력을 갖게 되고, 그로 인해 행성의 운명이 걸린 거대한 전쟁에 뛰어들게 되는데… 2012년 3월, 전 우주를 뒤흔들 거대 전쟁의 서막이 오른다!","movie_released_date":"2012-03-07","genre":"['액션', '모험', 'SF']"},{"id":1424,"movie_id":467244,"movie_title":"더 존 오브 인터레스트","overview":"","movie_released_date":"2023-05-19","genre":"['드라마', '역사', '전쟁']"},{"id":1496,"movie_id":28609,"movie_title":"드래곤볼 Z: 데드존 (구극장판 1기)","overview":"과거 지구의 신과 라이벌이었던 갈릭이라는 자가 있었다. 현재 지구의 신이 신의 후계자가 되자 갈릭은 마족을 모아 신에게 반항했다가 패배하고 300년 뒤에 돌아오겠다는 말을 남기고 사라졌다. 그 가릭의 아들인 갈릭 주니어가 드래곤볼을 모아 영원한 생명을 얻은 뒤, 세계를 지배하겠다는 야욕에 불타게 된다. 한편, 드래곤볼을 찾고 있던 갈릭의 부하들에게 손오반이 납치당했기 때문에 손오공은 오반을 찾아 갈릭의 성에 쳐들어간다.","movie_released_date":"1989-07-15","genre":"['애니메이션', '액션', '판타지']"}]
    '''
    
    # 만약 일치하는 데이터가 없다면 []가 반환된다.
    # [2] : [1]의 검색 결과에서 타이틀의 ID를 가져온다.
    # 각 영화의 movie_id를 사용하여 해당하는 Still을 가져오는 방법은 다음과 같습니다. 코드를 수정하여 movie_ids 변수에 영화들의 movie_id를 저장한 후, 해당 movie_ids를 사용하여 Still을 필터링하고 직렬화합니다.
    
    # 아래 코드는 튜플의 형태로 ids 
    movie_ids = movies.values_list('id', flat=True)
    #<QuerySet [16, 116, 151, 262]>
    
    
    
    # [3] : [2]의 ID를 가진 STILL을 가져오고 이것을 SERIALIZER.DATA로 보낸다. 
    if not movie_ids:
        return Response({"message": "No movies Found."})

    stills = Still.objects.filter(movie_id__in=movie_ids)
    if not stills:
        # Return appropriate response when no stills found
        return Response({"message": "No stills found for the given movie_ids."})

    # Serialize the Still queryset
    still_serializer = StillSerializer(stills, many=True)
    return Response(still_serializer.data)



def still_detail(request, stillId):
    still = Still.objects.get(id=stillId)
    still_serializer = StillSerializer(still)
    # 영화 Id 받아오기
    movieId = still_serializer.data['movie_id']
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
    recommend_still_list = Still.objects.filter(still_color__in=recommend_color)
    serializer = StillSerializer(recommend_still_list, many=True)
    # 만약 일치하는 데이터가 없다면 []가 반환된다.
    return JsonResponse(serializer.data, safe=False)


'''
MyPage에서 유저가 작성한 still을 반환하는 API:
1. 유저가 작성한 모든 스틸을 반환합니다.
'''
@api_view(['GET'])
def user_still(request, username):
    print('♧'* 100)
    print(username)
    # username을 가지고 User 모델에서 user id를 가져온다
    user = User.objects.get(username=username)
    stills = Still.objects.filter(user=user.id)
    serializer = StillSerializer(stills, many=True)
    return JsonResponse(serializer.data, safe=False)


'''
MyPage에서 유저가 새로운 Collection을 생성하는 API:
1. 유저는 NEW Collection을 제출합니다.
2. 테이블에 Collections 을 생성합니다.

'''



'''
MyPage에서 유저가 Collection에 Stills

'''
def create_collections(request):
    pass