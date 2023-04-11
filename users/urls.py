from . import views
from django.urls import path, include

app_name = 'users'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path("users/login/google", views.home, name='google-login'),
    path("logout" , views.logout_view)
]
