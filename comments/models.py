from django.db import models
from participants.models import Participant
from django.contrib.auth.models import User

class Comment(models.Model):
    auther = models.ForeignKey(Participant)
    content = TextField(max_length=250)
    liked_by = models.ManyToManyField(User)
    likes_number = liked_by.count()
    disliked_by = models.ManyToManyField(User)
    dislikes_number = disliked_by.count()
    
    def __str__(self):
        return self.Participant_Name