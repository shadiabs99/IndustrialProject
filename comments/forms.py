from django.forms import ModelForm
from .models import Comment

class CommentForm(ModelForm):
    def __init__(self, *args, **kwargs): 
        super(CommentForm, self).__init__(*args, **kwargs)                       
        self.fields['idea_id'].disabled = True
    class Meta:
        model = Comment
        fields = ['content', 'idea_id']