from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'comments'

urlpatterns = [
    path('', views.list_of_comments, name='list_of_comments'),
    path('details/<int:comment_id>', views.comment_details, name='comment_details'),
]
