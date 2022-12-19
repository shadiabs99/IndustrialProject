from django.db import models
from campaigns.models import Campaign
from comments.models import Comment
from django.contrib.auth.models import User

class Idea(models.Model):
    campaign = models.ForeignKey(Campaign)
    title = models.CharField(max_length=50)
    descrption = models.TextField(max_length=250)
    liked_by = models.ManyToManyField(User)
    likes_number = liked_by.count()
    disliked_by = models.ManyToManyField(User)
    dislikes_number = disliked_by.count()
    
    def __str__(self):
        return self.descrption

