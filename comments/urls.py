from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
app_name = 'comments'

urlpatterns = [
    path('', views.list_of_comments, name='list_of_comments'),
    path('<int:comment_id>/', views.comment_details, name='comment_details'),
    path('<int:comment_id>/delete/', views.comment_delete, name='comment_delete'),
    path('<int:comment_id>/update/', views.comment_update, name='comment_update'),
]
