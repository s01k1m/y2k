from django.urls import path
from . import views

urlpatterns = [
    # 홈 영화 검색
    path('search/<str:search_query>/', views.searchMovie, name='searchMovie'),
    # 홈 main 컬러
    path('<str:colorChoice>/', views.still_list, name='still_list'),
    # still detail
    path('detail/<int:stillId>/', views.still_detail, name='still_detail'),
    # still detail 하단 추천
    path('recommend/<str:color>/', views.recommend_still, name='recommend_still'),
    # user MyPage still
    path('user/<str:username>/stills/', views.user_still, name='user_still'),
    # user MyPage create collection
    path('user/<str:username>/createcollection/', views.create_collections, name='create_collection'),
    # user MyPage get all collections
    
]