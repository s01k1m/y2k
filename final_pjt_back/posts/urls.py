from django.urls import path
from . import views


urlpatterns = [
    path("", views.post, name="post"),
    path("getmovie/<str:search_query>/",views.movie_for_create, name='find_movie'),
]

'''
from django.urls import path
from . import views

app_name='movies'
urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
    path('<int:pk>/', views.detail, name="detail"),
    path('<int:pk>/update/', views.update, name="update"),
    path('<int:pk>/delete/', views.delete, name="delete"),
]

'''
