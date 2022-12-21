from django.db import models

class Participant(models.Model):
    name = models.CharField(max_length=50)
    birth_date = models.DateField()
    liked_ideas = models.ManyToManyField("ideas.Idea", related_name="liked_by_participants") 
    campaigns = models.ManyToManyField("campaigns.Campaign")
    #ideas = models.ManyToOneRel("ideas.Idea", related_name="auther_of_idea")
    
    def __str__(self):
        return self.name
