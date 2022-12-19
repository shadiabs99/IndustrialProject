from django.db import models

class Participant(models.Model):
    Participant_Name = models.CharField(max_length=50)
    Participant_BirthDate = models.DateField()

    def __str__(self):
        return self.Participant_Name

class Campaign(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    start_date = models.DateField()
    end_date = models.DateField()
    participants = models.ManyToManyField(Participant)

    def __str__(self):
        return self.title

