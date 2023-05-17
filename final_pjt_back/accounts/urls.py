from django.urls import include, path
from . import views

urlpatterns = [
    path('/', views.index, name='login'), # 로그인 페이지로 이동
    path('/signup', views.index, name='signup'), # 회원가입 페이지로 이동
]
