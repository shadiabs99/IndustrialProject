from allauth.account.views import SignupView
from .forms import CustomSignupForm
from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Profile

class CustomSignupView(SignupView):
    form_class = CustomSignupForm
    template_name = 'account/signup.html'  # Use your desired template

def user_profile(request):
    profile = Profile.objects.get(user_id=request.user.id)
    return render(request, 'profiles/profile.html', {'profile': profile})