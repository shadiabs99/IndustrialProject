from django.shortcuts import render
#from .models import Participant
from .models import Campaign
from django.shortcuts import get_object_or_404
# Create your views here.

def list_of_campaigns(request):
    campaigns = Campaign.objects.all()
    context = {'campaigns': campaigns}
    return render(request, 'campaigns/home.html', context)

def campaign_details(request, campaign_id):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    context = {'campaign': campaign}
    return render(request, 'campaigns/campaign_details.html', context)