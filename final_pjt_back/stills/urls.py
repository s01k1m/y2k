from django.urls import path
from . import views

urlpatterns = [
    path('', views.still_list, name='still_list'),
    path('<str:colorChoice>/', views.still_of_color, name='still_of_color'),
]