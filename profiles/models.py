from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/profile_pics/', null=True, blank=True, default='media/profile_pics/default_profile_picture.png')    
    
    class Meta:
        unique_together = ('user',)

