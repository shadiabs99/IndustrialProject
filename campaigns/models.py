from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes import fields

class Campaign(models.Model):
    auther = models.ForeignKey(User, on_delete=models.CASCADE, related_name="campaign_auther")
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    start_date = models.DateField()
    end_date = models.DateField()
    image = models.ImageField(upload_to =f'images/')
    token = models.CharField(max_length=10)
    
    def __str__(self):
        return self.title

