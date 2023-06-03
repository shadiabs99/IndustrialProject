from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
app_name = 'campaigns'
from ideas import views as idea_views

urlpatterns = [
    path('', views.list_of_campaigns, name='list_of_campaigns'),
    path('<int:campaign_id>/', views.campaign_details, name='campaign_details'),
    path('<int:campaign_id>/delete/', views.campaign_delete, name='campaign_delete'),
    path('<int:campaign_id>/update/', views.campaign_update, name='campaign_update'),
    path('<int:campaign_id>/like/', views.campaign_like, name='campaign_like'),
    path('<int:campaign_id>/update_image/', views.update_image, name='update-image'),
    path('<int:campaign_id>/ideas/', include('ideas.urls')),
    path('<int:campaign_id>/participate/', views.campaign_participate, name='campaign-participate'),   

]
