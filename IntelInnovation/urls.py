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
# from users import views as users_views
from campaigns import views as campaign_views
from ideas import views as idea_views
from comments import views as comment_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from profiles.views import CustomSignupView
from profiles import views as profile_views

urlpatterns = [
     # Other Views
     path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
     path("accounts/", include("allauth.urls")),
     path('admin/', admin.site.urls),
     path('users/', include('django.contrib.auth.urls')),
     path('profile/', profile_views.user_profile, name='user_profile'),

     # Campaign Views
     path('', campaign_views.list_of_campaigns, name='list_of_campaigns'),
     path('campaigns/', include('campaigns.urls')),
     path('top_campaigns/', campaign_views.list_of_top_campaigns, name='top_campaigns'),
     path('soon_campaigns/', campaign_views.list_of_soon_campaigns, name='soon_campaigns'),
     path('create', campaign_views.campaign_create, name='campaign_create'),
     path('archived_campaigns', campaign_views.archived_campaigns, name='archived_campaigns'),
     path('campaigns/<int:campaign_id>/remove_favorite/', campaign_views.remove_favorite_campaign, name='remove_favorite_campaign'),
     path('campaigns/<int:campaign_id>/add_favorite/', campaign_views.add_favorite_campaign, name='add_favorite_campaign'),

     # Idea Views
     path('ideas/', include('ideas.urls')),
     path('campaigns/<int:campaign_id>/ideas/create/', idea_views.idea_create, name='idea-create'),
     path('campaigns/<int:campaign_id>/ideas/<int:idea_id>/like/', idea_views.idea_like, name='idea-like'),
     path('campaigns/<int:campaign_id>/ideas/<int:idea_id>/', idea_views.idea_details, name='idea_details'),
     path('campaigns/<int:campaign_id>/ideas/<int:idea_id>/update/', idea_views.idea_update, name='idea_update'),
     path('campaigns/<int:campaign_id>/ideas/<int:idea_id>/remove_favorite/', idea_views.remove_favorite_idea, name='remove_favorite_idea'),
     path('campaigns/<int:campaign_id>/ideas/<int:idea_id>/add_favorite/', idea_views.add_favorite_idea, name='add_favorite_idea'),

     # Comment Views
     path('comments/', include('comments.urls')),
     path('campaigns/<int:campaign_id>/ideas/<int:idea_id>/comments/create', comment_views.comment_create, name='comment_create'),
     path('campaigns/<int:campaign_id>/ideas/<int:idea_id>/comments/top_comments', comment_views.top_comments, name='top_comments'),
     path('campaigns/<int:campaign_id>/ideas/<int:idea_id>/comments/<int:comment_id>/like/', comment_views.comment_like, name='comment-like'),
     path('campaigns/<int:campaign_id>/ideas/<int:idea_id>/comments/<int:comment_id>/reply/', comment_views.comment_create, name='comment_create'),
     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
