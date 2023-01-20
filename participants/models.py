from django.db import models
from django.contrib.auth.models import User
from campaigns.models import Campaign

class Participant(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    liked_campaigns = models.ManyToManyField(Campaign, related_name="liked_campaigns")
    liked_ideas = models.ManyToManyField(Campaign, related_name="liked_ideas")
    liked_comments = models.ManyToManyField(Campaign, related_name="liked_comments")
    
    def __str__(self):
        return self.user.username
    
