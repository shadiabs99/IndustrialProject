from django.urls import path
from . import views

app_name = 'campaigns'

urlpatterns = [
    path('', views.listOfCampaigns, name='campaigns'),
    path('details/<int:campaign_id>', views.campaign_details, name='campaign_details'),
]
