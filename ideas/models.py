from django.db import models

class Idea(models.Model):
    campaign = models.ForeignKey("campaigns.Campaign", on_delete=models.CASCADE)
    auther = models.ForeignKey("participants.Participant", on_delete=models.CASCADE, related_name="auther_of_idea")
    title = models.CharField(max_length=50)
    descrption = models.TextField(max_length=250)
    liked_by = models.ManyToManyField("participants.Participant", related_name="liked_by_participants")
    
    def __str__(self):
        return self.descrption

