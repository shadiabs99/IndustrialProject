from django.shortcuts import render
from .forms import IdeaForm
from .models import Idea, IdeaLike
from django.shortcuts import get_object_or_404, redirect
from campaigns.models import Campaign, Like
from comments.models import Comment
from django.db.models import Count

import re


def list_of_ideas(request, campaign_id):
    ideas = Idea.objects.all().filter(campaign_id=campaign_id)
    context = {'ideas': ideas, 'campaign_id': campaign_id}
    return render(request, 'campaigns/campaign_details.html', context)


def list_of_top_ideas(request):
    top_ideas = Idea.objects.annotate(
        q_count=Count('likes')).order_by('-q_count')[:7]
    context = {'ideas': top_ideas}
    return render(request, 'campaigns/campaign_details.html', context)


def idea_details(request, idea_id, campaign_id):
    idea = get_object_or_404(Idea, id=idea_id)
    comments = Comment.objects.all().filter(idea_id=idea_id)
    if request.method == 'GET':
        form = IdeaForm(instance=idea)
        context = {'form': form, 'idea': idea,
                   'campaign_id': campaign_id, 'comments': comments}
        return render(request, 'ideas/idea_details.html', context)
    else:
        try:
            form = IdeaForm(request.POST, instance=idea)
            form.save()
            return redirect('ideas:list_of_ideas', campaign_id)
        except ValueError:
            context = {'form': IdeaForm(), 'error': 'Bad data try again'}
            return render(request, 'ideas/idea_details.html', context)


def idea_create(request, campaign_id):
    user = request.user

    if request.method == 'GET':
        form = IdeaForm(initial={'campaign_id': campaign_id})
        field = form.fields['campaign_id']
        field.widget = field.hidden_widget()
        return render(request, 'ideas/idea_form.html', {'form': form})
    else:
        try:
            form = IdeaForm(request.POST, request.FILES,
                            initial={'campaign_id': campaign_id})
            field = form.fields['campaign_id']
            field.widget = field.hidden_widget()
            form.save()
            return redirect('campaigns:campaign_details', campaign_id)
        except ValueError:
            context = {'form': IdeaForm(), 'error': 'Bad data try again'}
            return render(request, 'ideas/idea_form.html', context)


def idea_delete(request, idea_id, campaign_id):
    idea = get_object_or_404(Idea, id=idea_id)
    idea.delete()
    return redirect('ideas:list_of_ideas', campaign_id)


def idea_update(request, idea_id, campaign_id):
    idea = Idea.objects.get(id=idea_id)
    form = IdeaForm(request.POST if request.POST else None, instance=idea)
    field = form.fields['campaign_id']
    field.widget = field.hidden_widget()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('campaigns:campaign_details', campaign_id)
    return render(request, 'ideas/idea_update.html', {'form': form})


def idea_like(request, campaign_id, idea_id):
    user = request.user
    if request.method == 'POST':

        idea = Idea.objects.get(id=idea_id)

        if user in idea.likes.all():
            idea.likes.remove(user)
        else:
            idea.likes.add(user)
        like, created = IdeaLike.objects.get_or_create(
            user=user, idea_id=idea_id)
        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
        like.save()
    return redirect('idea_details', campaign_id, idea_id)
