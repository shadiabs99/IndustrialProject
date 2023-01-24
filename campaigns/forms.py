from django.forms import ModelForm
from .models import Campaign
from django.db import models
from django.forms import fields
from django import forms


class CampaignForm(ModelForm):
    class Meta:

        model = Campaign
        fields = ['manager', 'title', 'description',
                  'start_date', 'end_date', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',
                                            'style': 'width: auto',
                                            'style': 'width: auto',
                                            'placeholder': 'Title',
                                            }),
            'description': forms.Textarea(attrs={'class': 'form-control',
                                                 'style': 'width: auto',
                                                 'placeholder': 'Description', }),
            'start_date': forms.SelectDateWidget(),
            'end_date': forms.SelectDateWidget(),

        }

        labels = {
            'manager': 'Who manages this campaign?',
            'title': '',
            'description': '',
            'start_date': 'Start Date: ',
            'end_date': 'End Date: ',
        }


class UserImage(forms.ModelForm):
    class meta:
        models = Campaign
        fields = '__all__'
