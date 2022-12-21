from django.shortcuts import render
from .models import Participant
from django.shortcuts import get_object_or_404

def list_of_participants(request):
    participants = Participant.objects.all()
    context = {'participants': participants}
    return render(request, 'participants/home.html', context)

def participant_details(request, participant_id):
    participant = get_object_or_404(Participant, id=participant_id)
    context = {'participant': participant}
    return render(request, 'participants/participant_details.html', context)