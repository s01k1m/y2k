from django.urls import path
from . import views

urlpatterns = [
    # path('ALL/', views.still_list, name='still_list'),
    path('search/<str:search_query>/', views.searchMovie, name='searchMovie'),
    path('<str:colorChoice>/', views.still_list, name='still_list'),
]