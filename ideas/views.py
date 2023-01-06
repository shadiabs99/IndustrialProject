from django.shortcuts import render
from .forms import IdeaForm
from .models import Idea
from django.shortcuts import get_object_or_404, redirect

def list_of_ideas(request):
    ideas = Idea.objects.all()
    context = {'ideas': ideas}
    return render(request, 'ideas/home.html', context)

def idea_details(request, idea_id):
    idea = get_object_or_404(Idea, id=idea_id)
    
    if request.method == 'GET':
        form = IdeaForm(instance=idea)
        context =  {'form': form, 'idea': idea}
        return render(request, 'ideas/idea_details.html', context)
    else:
        try:
            form = IdeaForm(request.POST, instance=idea)
            form.save()
            return redirect('ideas:list_of_ideas')
        except ValueError:
            context = {'form': IdeaForm(), 'error': 'Bad data try again'}
            return render(request, 'ideas/idea_details.html', context)
    

def idea_create(request):
    if request.method == 'GET':
        return render(request, 'ideas/idea_form.html', {'form': IdeaForm()})
    else:
        try:
            form = IdeaForm(request.POST)
            form.save()
            return redirect('ideas:list_of_ideas')
        except ValueError:
            context = {'form': IdeaForm(), 'error': 'Bad data try again'}
            return render(request, 'ideas/idea_form.html', context)
        
def idea_delete(request, idea_id):
    idea = get_object_or_404(Idea, id=idea_id)
    idea.delete()
    return redirect('ideas:list_of_ideas')
