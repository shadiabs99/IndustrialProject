from django.shortcuts import render
from .models import Idea
from django.shortcuts import get_object_or_404

# Create your views here.

def list_of_ideas(request):
    idea = Idea.objects.all()
    context = {'ideas': ideas}
    return render(request, 'ideas/home.html', context)

def idea_detailes(request, idea_id):
    idea = get_object_or_404(Idea, id=idea_id)
    context = {'idea': idea}
    return render(request, 'ideas/idea_detailes.html', context)