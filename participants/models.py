from django.db import models
#import ideas.models

class Participant(models.Model):
    name = models.CharField(max_length=50)
    birth_date = models.DateField()
    #liked_ideas = models.ManyToManyField(Idea) 

    def __str__(self):
        return self.name
