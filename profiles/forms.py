from allauth.account.forms import SignupForm
from .models import Profile
from django import forms

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name', required=True)
    last_name = forms.CharField(max_length=30, label='Last Name', required=True)
    profile_image = forms.ImageField(label='Profile Image')
    
    def save(self, request):
        user = super().save(request)
        image = self.cleaned_data['profile_image']
        profile = Profile(user=user, image=image)
        profile.save()
        return user
