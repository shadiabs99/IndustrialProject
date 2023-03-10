from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model, login, logout, authenticate
from campaigns.models import Campaign
def signup(request):
    if request.method == 'GET':
        return render(request, 'registration/signup.html',
                      {'form': UserCreationForm()})
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            authenticate(username=username, password=raw_password)
            user = get_user_model().objects.get(username=username)
            login(request, user)
            campaigns = Campaign.objects.all()
            context = {'campaigns': campaigns}
            return render(request,'campaigns/home.html', context=context)
        else:
            error = form.errors
            return render(request, 'registration/signup.html', {'form':UserCreationForm(), 'error': error})
        
        
