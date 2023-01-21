from django.db import models
from participants.models import Participant
from ideas.models import Idea
from author.decorators import with_author

@with_author
class Comment(models.Model):
    content = models.TextField(max_length=250)
    idea_id = models.IntegerField(null=True)
    
    def __str__(self):
        return self.content