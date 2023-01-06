from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'campaigns'

urlpatterns = [
    path('', views.list_of_campaigns, name='list_of_campaigns'),
    path('details/<int:campaign_id>', views.campaign_details, name='campaign_details'),
    path('create/', views.campaign_create, name='campaign_create'),
    path('delete/<int:campaign_id>', views.campaign_delete, name='campaign_delete'),
]