"""IntelInnovation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as users_views

urlpatterns = [
    path('', include('campaigns.urls')),
    path('admin/', admin.site.urls),
    path('campaigns/', include('campaigns.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('users/signup/', users_views.signup, name='signup'),
    
]
