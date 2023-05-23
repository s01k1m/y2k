from django.urls import path
from . import views

urlpatterns = [
    path('<int:still_id>/', views.comment_create_or_view, name='comment_create_or_view'),
    path('<int:comment_id>/delete/', views.comment_delete, name='comment_delete'),
]