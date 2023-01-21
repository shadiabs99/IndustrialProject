from django.shortcuts import render
from .forms import CampaignForm
from .models import Campaign, Like, Participant
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
import ideas.views
from ideas.models import Idea
from django.db.models import Count
import os

def list_of_campaigns(request):
    campaigns = Campaign.objects.all()
    context = {'campaigns': campaigns}
    return render(request, 'campaigns/home.html', context)

def list_of_top_campaigns(request):
    top_campaigns = Campaign.objects.annotate(q_count=Count('likes')).order_by('-q_count')[:7]    
    context = {'campaigns': top_campaigns}
    return render(request, 'campaigns/home.html', context)

def campaign_details(request, campaign_id):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    user = request.user
    ideas = Idea.objects.all().filter(campaign_id=campaign_id)
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
    if request.method == 'GET':
        return render(request, 'campaigns/campaign_form.html', {'form': CampaignForm()})
    else:
        try:
            form = CampaignForm(request.POST, request.FILES)
            form.save()
            return redirect('campaigns:list_of_campaigns')
        except ValueError:
            context = {'form': CampaignForm(), 'error': 'Bad data try again'}
            return render(request, 'campaigns/campaign_form.html', context)
        
def campaign_delete(request, campaign_id):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    campaign.delete()
    return redirect('campaigns:list_of_campaigns')
    
def request_page(request):
    if(request.GET.get('mybtn')):
        mypythoncode.mypythonfunction( int(request.GET.get('mytextbox')) )
        return render(request,'ideas/ideas_list.html')

def campaign_update(request, campaign_id):
    campaign = Campaign.objects.get(id=campaign_id)
    form = CampaignForm(request.POST if request.POST else None, instance=campaign)
    if request.method == 'POST':
        if form.is_valid():
            image_path = campaign.image.path
            if os.path.exists(image_path):
                os.remove(image_path)
            form.save()
            return redirect('campaigns:campaign_details', campaign.id)    
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

def campaign_participate(request, campaign_id):
    user = request.user
    if request.method == 'POST':
        
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
