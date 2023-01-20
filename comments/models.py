from django.db import models
from participants.models import Participant
from ideas.models import Idea


class Comment(models.Model):
    #auther = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name="comment_auther")
    content = models.TextField(max_length=250)
    #idea = models.ForeignKey(Idea, on_delete=models.CASCADE, related_name="comment_idea")
    
    def __str__(self):
        return self.content