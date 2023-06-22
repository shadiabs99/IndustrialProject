from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    image = models.ImageField(upload_to='media/profile_pics/', null=True, blank=True, default='media/profile_pics/default_profile_picture.png')    
    score = models.IntegerField(default=0)
    
    class Meta:
        unique_together = ('user',)

