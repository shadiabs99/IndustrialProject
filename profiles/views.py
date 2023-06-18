from allauth.account.views import SignupView
from .forms import CustomSignupForm
from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Profile
from django.contrib.auth.decorators import login_required
from campaigns.models import Campaign
from ideas.models import Idea
from comments.models import Comment

class CustomSignupView(SignupView):
    form_class = CustomSignupForm
    template_name = 'account/signup.html'  # Use your desired template

@login_required
def user_profile(request):
    user = request.user
    profile = Profile.objects.get(user_id=user.id)
    favorite_campaigns = Campaign.objects.filter(favorites=user)
    favorite_ideas = Idea.objects.filter(idea_favorites=user)
    latest_comments = Comment.objects.filter(author=user).order_by('-created_at')[:3]
    participated_campaigns = Campaign.objects.filter(participants=user)
    context = {'participated_campaigns': participated_campaigns, 'profile': profile, 'favorite_campaigns': favorite_campaigns, 'favorite_ideas': favorite_ideas, 'latest_comments': latest_comments,}
    return render(request, 'profiles/profile.html', context)