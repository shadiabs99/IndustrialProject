from django.db import models
from campaigns.models import Campaign
from participants.models import Participant
from django.contrib.auth.models import User
from author.decorators import with_author

@with_author
class Idea(models.Model):
    idea_title = models.CharField(max_length=50)
    idea_description = models.TextField(max_length=250)
    idea_url = models.URLField()
    campaign_id = models.IntegerField(null=True)
    
    def __str__(self):
        return self.idea_description

