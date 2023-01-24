from django.forms import ModelForm
from .models import Idea
from django import forms


class IdeaForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(IdeaForm, self).__init__(*args, **kwargs)
        self.fields['campaign_id'].disabled = True

    class Meta:
        model = Idea
        fields = ['idea_title', 'idea_description', 'idea_url', 'campaign_id']
        widgets = {
            'idea_title': forms.TextInput(attrs={'class': 'form-control',
                                                 'style': 'width: auto',
                                                 'style': 'width: auto',
                                                 'placeholder': 'Title',
                                                 }),
            'idea_description': forms.Textarea(attrs={'class': 'form-control',
                                                      'style': 'width: auto',
                                                      'placeholder': 'Description', }),
            'idea_url': forms.TextInput(attrs={'class': 'form-control',
                                               'style': 'width: auto',
                                               'placeholder': 'URL', }),

        }

        labels = {
            'idea_title': '',
            'idea_description': '',
            'idea_url': '',

        }
