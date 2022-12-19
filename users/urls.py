from . import views
from django.urls import path, include
from django.conf import settings

app_name = 'users'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'),
]
