from django.db import models

class Participant(models.Model):
    Participant_Name = models.CharField(max_length=50)
    Participant_BirthDate = models.DateField()

    def __str__(self):
        return self.Participant_Name

class Campaign(models.Model):
    Campaign_Name = models.CharField(max_length=50)
    Description = models.TextField(max_length=250)
    Start_Date = models.DateField()
    End_Date = models.DateField()
    Participants = models.ManyToManyField(Participant)

    def __str__(self):
        return self.Campaign_Name

