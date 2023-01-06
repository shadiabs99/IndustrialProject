from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'ideas'

urlpatterns = [
    path('', views.list_of_ideas, name='list_of_campaigns'),
    path('details/<int:idea_id>', views.idea_details, name='idea_details'),
    path('create/', views.idea_create, name='idea_create'),
    path('delete/<int:idea_id>', views.idea_delete, name='idea_delete'),
]
