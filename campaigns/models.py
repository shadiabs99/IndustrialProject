from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes import fields

class Campaign(models.Model):
    auther = models.ForeignKey(User, on_delete=models.CASCADE, related_name="campaign_auther")
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    start_date = models.DateField()
    end_date = models.DateField()
    image = models.ImageField(null=True, blank=True, upload_to ="images/")
    token = models.CharField(max_length=10)
    likes = models.ManyToManyField(User, default=None, blank=True, related_name="likes")
    
    def __str__(self):
        return self.title
    
    @property
    def num_likes(self):
        return self.likes.all().count()

LIKE_CHOICES = (
    ('Like', 'Like'), 
    ('Unlike', 'Unlike')
)
class Like (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)
    
    def __str__(self):
        return str(self.campaign)