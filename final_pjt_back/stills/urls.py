from django.urls import path
from . import views

urlpatterns = [
    # path('ALL/', views.still_list, name='still_list'),
    path('<str:colorChoice>/', views.still_list, name='still_list'),
]