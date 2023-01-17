from django.db import models
from campaigns.models import Campaign
from participants.models import Participant
from django.contrib.auth.models import User

class Idea(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name="idea_campaign")
    auther = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name="idea_auther")
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    url = models.URLField()
    
    def __str__(self):
        return self.description

