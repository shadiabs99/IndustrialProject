from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'campaigns'

urlpatterns = [
    path('', views.list_of_campaigns, name='campaigns'),
    path('details/<int:campaign_id>', views.campaign_details, name='campaign_details'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
]
