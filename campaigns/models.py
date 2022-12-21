from django.db import models

class Campaign(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    start_date = models.DateField()
    end_date = models.DateField()
    participants = models.ManyToManyField("participants.Participant")

    def __str__(self):
        return self.title

