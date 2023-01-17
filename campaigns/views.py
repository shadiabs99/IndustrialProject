from django.shortcuts import render
from .forms import CampaignForm
from .models import Campaign, Like
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

def list_of_campaigns(request):
    campaigns = Campaign.objects.all()
    context = {'campaigns': campaigns}
    return render(request, 'campaigns/home.html', context)

def campaign_details(request, campaign_id):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    user = request.user
    
    if request.method == 'GET':
        form = CampaignForm(instance=campaign)
        context =  {'form': form, 'campaign': campaign, 'user': user}
        return render(request, 'campaigns/campaign_details.html', context)
    else:
        try:
            form = CampaignForm(request.POST, instance=campaign)
            form.save()
            return redirect('campaigns:list_of_campaigns')
        except ValueError:
            context = {'form': CampaignForm(), 'error': 'Bad data try again'}
            return render(request, 'campaigns/campaign_details.html', context)
    
@login_required
def campaign_create(request):
    if request.method == 'GET':
        return render(request, 'campaigns/campaign_form.html', {'form': CampaignForm()})
    else:
        try:
            form = CampaignForm(request.POST)
            form.save()
            return redirect('campaigns:list_of_campaigns')
        except ValueError:
            context = {'form': CampaignForm(), 'error': 'Bad data try again'}
            return render(request, 'campaigns/campaign_form.html', context)
        
def campaign_delete(request, campaign_id):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    campaign.delete()
    return redirect('campaigns:list_of_campaigns')

def campaign_update(request, campaign_id):
    campaign = Campaign.objects.get(id=campaign_id)
    form = CampaignForm(instance=campaign)
    return render(request, 'campaigns/campaign_update.html', {'form': form})

def about_us(request):
    return render(request, 'campaigns/about_us.html')

def campaign_like(request, campaign_id):
    user = request.user
    if request.method == 'POST':
        
        campaign = Campaign.objects.get(id=campaign_id)
        
        if user in campaign.likes.all():
            campaign.likes.remove(user)
        else:
            campaign.likes.add(user)    
        like, created = Like.objects.get_or_create(user=user, campaign_id=campaign_id)
        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
        like.save()
        
    return redirect('campaigns:campaign_details', campaign_id)