from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes import fields
from author.decorators import with_author

@with_author
class Campaign(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name="campaign_manager")
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    start_date = models.DateField()
    end_date = models.DateField()
    image = models.ImageField(null=True, blank=True, upload_to ="images/")
    token = models.CharField(max_length=10)
    
    likes = models.ManyToManyField(User, default=None, blank=True, related_name="likes")
    participants = models.ManyToManyField(User, default=None, blank=True, related_name="campaign_participants")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    campaign_opened = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title
    
    @property
    def num_likes(self):
        return self.likes.all().count()
    
    @property
    def num_participants(self):
        return self.participants.all().count()

LIKE_CHOICES = (
    ('Like', 'Like'), 
    ('Unlike', 'Unlike')
)

PARTICIPATE_CHOICES = (
    ('Patrticipate', 'Patrticipate'), 
    ('Withdraw', 'Withdraw')
)
class Like (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)
    
    def __str__(self):
        return str(self.campaign)
    
class Participant (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    value = models.CharField(choices=PARTICIPATE_CHOICES, default='Patrticipate', max_length=100)
    
    def __str__(self):
        return str(self.campaign)