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
    path('user/<str:username>/collections/',
         views.user_collections, name='collection'),
    # detail page append still to collection
    path('append/<int:still_pk>/<int:collection_pk>/',
         views.add_still_to_collection, name='appendStill'),
    # DELETE COLLECTION
    path('user/<str:username>/collection/delete/<int:collection_pk>/', views.collection_view),

]
