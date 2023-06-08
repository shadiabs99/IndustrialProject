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
from campaigns import views as campaign_views
from ideas import views as idea_views
from comments import views as comment_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path("" , include("users.urls")),

    # Campaign Views
    path('', campaign_views.list_of_campaigns, name='list_of_campaigns'),
    path('admin/', admin.site.urls),
    path('campaigns/', include('campaigns.urls')),
    path('top_campaigns/', campaign_views.list_of_top_campaigns, name='top_campaigns'),
    path('soon_campaigns/', campaign_views.list_of_soon_campaigns, name='soon_campaigns'),
    path('ideas/', include('ideas.urls')),
    path('comments/', include('comments.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('users/signup/', users_views.signup, name='signup'),
    path('about_us', campaign_views.about_us, name='about_us'),
    path('create', campaign_views.campaign_create, name='campaign_create'),
    path('archived_campaigns', campaign_views.archived_campaigns, name='archived_campaigns'),


    # Idea Views
    path('campaigns/<int:campaign_id>/ideas/create/',
         idea_views.idea_create, name='idea-create'),
    path('campaigns/<int:campaign_id>/ideas/<int:idea_id>/like/',
         idea_views.idea_like, name='idea-like'),
    path('campaigns/<int:campaign_id>/ideas/<int:idea_id>/',
         idea_views.idea_details, name='idea_details'),


    # Comment Views
    path('campaigns/<int:campaign_id>/ideas/<int:idea_id>/comments/create',
         comment_views.comment_create, name='comment_create'),
    path('campaigns/<int:campaign_id>/ideas/<int:idea_id>/comments/top_comments',
         comment_views.list_of_top_comments, name='top-comments'),
    path('campaigns/<int:campaign_id>/ideas/<int:idea_id>/comments/<int:comment_id>',
         comment_views.comment_details, name='comment_details'),
    path('campaigns/<int:campaign_id>/ideas/<int:idea_id>/comments/<int:comment_id>/like/',
         comment_views.comment_like, name='comment-like'),
    path('campaigns/<int:campaign_id>/ideas/<int:idea_id>/comments/<int:comment_id>/reply/',
         comment_views.comment_create, name='comment_create'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
