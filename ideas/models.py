from django.db import models
from campaigns.models import Campaign
from participants.models import Participant
from django.contrib.auth.models import User
from author.decorators import with_author

@with_author
class Idea(models.Model):
    idea_title = models.CharField(max_length=50)
    # idea_description = models.TextField(max_length=250)
    idea_url = models.URLField()
    campaign_id = models.IntegerField(null=True)
    
    team = models.CharField(max_length=50)
    background = models.TextField(max_length=250)
    solution = models.TextField(max_length=250)
    impact = models.TextField(max_length=250)

    likes = models.ManyToManyField(User, default=None, blank=True, related_name="idea_likes")
    
    def __str__(self):
        return self.idea_description
    
    @property
    def num_likes(self):
        return self.likes.all().count()

LIKE_CHOICES = (
    ('Like', 'Like'), 
    ('Unlike', 'Unlike')
)

class IdeaLike (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)
    
    def __str__(self):
        """dsdsd"""
        return str(self.idea)