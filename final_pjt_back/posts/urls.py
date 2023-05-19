from django.urls import path
from . import views
from .views import APITest


urlpatterns = [
    path("", APITest.as_view(), name="post")
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