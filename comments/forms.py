from django.forms import ModelForm
from .models import Comment
from django import forms


class CommentForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['idea_id'].disabled = True
        self.fields['comment_id'].disabled = True

    class Meta:
        model = Comment
        fields = ['content', 'idea_id', 'comment_id']

        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control',
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
            'content': '',
            'idea_description': '',
            'idea_url': '',

        }
