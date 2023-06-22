from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
app_name = 'ideas'

urlpatterns = [
    path('', views.list_of_ideas, name='list_of_ideas'),
    path('<int:idea_id>/update/', views.idea_update, name='idea_update'),
    path('<int:idea_id>/comments/', include('comments.urls')),
    path('<int:idea_id>/delete/', views.idea_delete, name='idea_delete'),
]
