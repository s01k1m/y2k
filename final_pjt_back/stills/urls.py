from django.urls import path
from . import views

urlpatterns = [
    path('search/<str:search_query>/', views.searchMovie, name='searchMovie'),
    path('<str:colorChoice>/', views.still_list, name='still_list'),
    path('detail/<int:stillId>/', views.still_detail, name='still_detail'),
    path('recommend/<str:color>/', views.recommend_still, name='recommend_still'),
]