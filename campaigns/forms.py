from django.forms import ModelForm
from .models import Campaign
from django.db import models  
from django.forms import fields  
from django import forms  
class CampaignForm(ModelForm):
    class Meta:
        model = Campaign
        fields = ['manager', 'title', 'description', 'start_date', 'end_date', 'image', 'token']
        
class UserImage(forms.ModelForm):  
    class meta:  
        models = Campaign
        fields = '__all__'  