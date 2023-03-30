from django.forms import ModelForm
from .models import Idea
from django import forms


class IdeaForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(IdeaForm, self).__init__(*args, **kwargs)
        self.fields['campaign_id'].disabled = True

    class Meta:
        model = Idea
        fields = ['idea_title', 'idea_url',
                  'campaign_id', 'team', 'background', 'impact', 'solution']
        widgets = {
            'idea_title': forms.TextInput(attrs={'class': 'form-control',
                                                 'style': 'width: auto',
                                                 'style': 'width: auto',
                                                 'placeholder': 'Title',
                                                 }),
            'idea_url': forms.TextInput(attrs={'class': 'form-control',
                                               'style': 'width: auto',
                                               'placeholder': 'URL', }),
            'team': forms.TextInput(attrs={'class': 'form-control',
                                           'style': 'width: auto',
                                           'style': 'width: auto',
                                           'placeholder': 'Team',
                                           }),
            'background': forms.Textarea(attrs={'class': 'form-control',
                                                'style': 'width: auto',
                                                'placeholder': 'Background and Problem Statement', }),
            'solution': forms.Textarea(attrs={'class': 'form-control',
                                              'style': 'width: auto',
                                              'placeholder': 'Proposed Solution', }),
            'impact': forms.Textarea(attrs={'class': 'form-control',
                                            'style': 'width: auto',
                                            'placeholder': 'Impact', }),

        }

        labels = {
            'idea_title': 'Title',
            'idea_url': 'URL',
            'team': 'Team',
            'background': 'Background',
            'solution': 'Solution',
            'impact': 'Impact',

        }
