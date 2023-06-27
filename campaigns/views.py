from django.shortcuts import render
from .forms import CampaignForm
from .models import Campaign, Like, Participant
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
import ideas.views
from ideas.models import Idea
from django.db.models import Count
import os
from profiles.models import Profile
from IntelInnovation.common import Score
from django.core.exceptions import PermissionDenied

def list_of_top_campaigns(request):
    top_campaigns = Campaign.objects.annotate(q_count=Count('likes')).order_by('-q_count')[:7]
    context = {'campaigns': top_campaigns}
    return render(request, 'campaigns/home.html', context)

def list_of_campaigns(request):
    top_campaigns = Campaign.objects.all().order_by('-created_at')
    context = {'campaigns': top_campaigns}
    return render(request, 'campaigns/home.html', context)

def archived_campaigns(request):
    campaigns = Campaign.objects.all().order_by('-created_at')
    context = {'campaigns': campaigns}
    return render(request, 'campaigns/archived_campaigns.html', context)

def list_of_soon_campaigns(request):
    campaigns = Campaign.objects.all().order_by('start_date')
    context = {'campaigns': campaigns}
    return render(request, 'campaigns/home.html', context)

def campaign_details(request, campaign_id):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    user = request.user
    ideas = Idea.objects.all().filter(campaign_id=campaign_id).order_by('-idea_created_at')

    if request.method == 'GET':
        form = CampaignForm(instance=campaign)
        context =  {'form': form, 'campaign': campaign, 'user': user, 'ideas': ideas}
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
    user = request.user
    profile = Profile.objects.get(user_id=user.id)
    if request.method == 'GET':
        return render(request, 'campaigns/campaign_form.html', {'form': CampaignForm()})
    else:
        try:
            profile.score = profile.score + Score.NEW_CAMOAIGN.value
            profile.save()
            form = CampaignForm(request.POST, request.FILES)
            form.save()
            return redirect('campaigns:list_of_campaigns')
        except ValueError:
            context = {'form': CampaignForm(), 'error': 'Bad data try again'}
            return render(request, 'campaigns/campaign_form.html', context)

@login_required
def campaign_delete(request, campaign_id):
    if campaign.manager == request.user or campaign.author == request.user:
        campaign = get_object_or_404(Campaign, id=campaign_id)
        campaign.delete()
        return redirect('campaigns:list_of_campaigns')
    else:
        raise PermissionDenied
    
@login_required
def campaign_close(request, campaign_id):
    if campaign.manager == request.user or campaign.author == request.user:
        campaign = get_object_or_404(Campaign, id=campaign_id)
        campaign.campaign_opened = False
        campaign.save()
        return redirect('campaigns:list_of_campaigns')
    else:
        raise PermissionDenied

@login_required
def campaign_update(request, campaign_id):
    campaign = Campaign.objects.get(id=campaign_id)
    if campaign.manager == request.user or campaign.author == request.user:
        form = CampaignForm(request.POST if request.POST else None, instance=campaign)
        if request.method == 'POST':
            if form.is_valid():
                image_path = campaign.image.url
                if os.path.exists(image_path):
                    os.remove(image_path)
                form.save()
                return redirect('campaigns:campaign_details', campaign.id)
        return render(request, 'campaigns/campaign_update.html', {'form': form})
    else:
        raise PermissionDenied

@login_required()
def campaign_like(request, campaign_id):
    user = request.user

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
    
@login_required()
def campaign_participate(request, campaign_id):
    user = request.user

    campaign = Campaign.objects.get(id=campaign_id)

    if user in campaign.participants.all():
        campaign.participants.remove(user)
    else:
        campaign.participants.add(user)
    participant, created = Participant.objects.get_or_create(user=user, campaign_id=campaign_id)
    if not created:
        if participant.value == 'Patrticipate':
            participant.value = 'Withdraw'
        else:
            participant.value = 'Patrticipate'
    participant.save()
    return redirect('campaigns:campaign_details', campaign_id)

@login_required
def update_image(request, campaign_id):
    campaign = Campaign.objects.get(id=campaign_id)
    form = CampaignForm(request.POST, request.FILES, instance=campaign)

    if form.is_valid():

        # deleting old uploaded image.
        image_path = campaign.image.image_document.path
        if os.path.exists(image_path):
            os.remove(image_path)

        # the `form.save` will also update your newest image & path.
        form.save()
        return redirect("list_of_campaigns")
    else:
        context = {'campaign': campaign, 'form': form}
        return render(request, 'campaigns/campaign_update.html', context)

@login_required
def add_favorite_campaign(request, campaign_id):
    campaign = get_object_or_404(Campaign, pk=campaign_id)
    campaign.favorites.add(request.user)
    return redirect('campaigns:campaign_details', campaign_id)

@login_required
def remove_favorite_campaign(request, campaign_id):
    campaign = get_object_or_404(Campaign, pk=campaign_id)
    campaign.favorites.remove(request.user)
    return redirect('campaigns:campaign_details', campaign_id)