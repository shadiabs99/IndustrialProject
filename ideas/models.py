from django.db import models
#import campaigns.models 
#import comments.models 
#import participants.models 

class Idea(models.Model):
    #campaign = models.ForeignKey(Campaign, on_delete=models.SET_DEFAULT)
    #auther = 
    title = models.CharField(max_length=50)
    descrption = models.TextField(max_length=250)
    #liked_by = models.ManyToManyField(Participant)
    
    def __str__(self):
        return self.descrption

