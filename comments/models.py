from django.db import models
#from campaigns.models import Participant

class Comment(models.Model):
    #auther = models.ForeignKey(Participant, on_delete=models.SET_DEFAULT)
    content = models.TextField(max_length=250)
    #liked_by = models.ManyToManyField(Participant)
    
    def __str__(self):
        return self.Participant_Name