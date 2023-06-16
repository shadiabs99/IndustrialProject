from django.shortcuts import render
from .forms import IdeaForm
from .models import Idea, IdeaLike
from django.shortcuts import get_object_or_404, redirect
from campaigns.models import Campaign, Like
from comments.models import Comment
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import re


def list_of_ideas(request, campaign_id):
    ideas = Idea.objects.all().order_by('idea_created_at')
    context = {'ideas': ideas}
    return render(request, 'campaigns/campaign_details.html', context)


def list_of_top_ideas(request, campaign_id):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    top_ideas = Idea.objects.annotate(q_count=Count('idea_likes')).order_by('-q_count')[:7]
    context = {'ideas': top_ideas, 'campaign': campaign}
    return render(request, 'campaigns/campaign_details.html', context)


def idea_details(request, idea_id, campaign_id):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    idea = get_object_or_404(Idea, id=idea_id)
    comments = Comment.objects.all().filter(idea_id=idea_id)
    comments = comments.order_by('-created_at')

    if request.method == 'GET':
        form = IdeaForm(instance=idea)
        context = {'form': form, 'idea': idea,
                    'campaign': campaign, 'comments': comments}
        return render(request, 'ideas/idea_details.html', context)
    else:
        try:
            form = IdeaForm(request.POST, instance=idea)
            form.save()
            return redirect('ideas:list_of_ideas', campaign_id)
        except ValueError:
            context = {'form': IdeaForm(), 'error': 'Bad data try again'}
            return render(request, 'ideas/idea_details.html', context)

def idea_details_top_comments(request, idea_id, campaign_id):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    idea = get_object_or_404(Idea, id=idea_id)
    comments = Comment.objects.all().filter(idea_id=idea_id).annotate(q_count=Count('likes')).order_by('-q_count')[:7]

    if request.method == 'GET':
        form = IdeaForm(instance=idea)
        context = {'form': form, 'idea': idea,
                    'campaign': campaign, 'comments': comments}
        return render(request, 'ideas/idea_details.html', context)
    else:
        try:
            form = IdeaForm(request.POST, instance=idea)
            form.save()
            return redirect('ideas:list_of_ideas', campaign_id)
        except ValueError:
            context = { 'campaign': campaign, 'form': IdeaForm(), 'error': 'Bad data try again'}
            return render(request, 'ideas/idea_details.html', context)
        
@login_required
def idea_create(request, campaign_id):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    user = request.user

    if request.method == 'GET':
        form = IdeaForm(initial={'campaign_id': campaign_id})
        field = form.fields['campaign_id']
        field.widget = field.hidden_widget()
        return render(request, 'ideas/idea_form.html', {'form': form, 'campaign': campaign})
    else:
        try:
            form = IdeaForm(request.POST, request.FILES,
                            initial={'campaign_id': campaign_id})
            field = form.fields['campaign_id']
            field.widget = field.hidden_widget()
            form.save()
            return redirect('campaigns:campaign_details', campaign_id)
        except ValueError:
            context = {'form': IdeaForm(), 'error': 'Bad data try again', 'campaign': campaign}
            return render(request, 'ideas/idea_form.html', context)

@login_required
def idea_delete(request, idea_id, campaign_id):
    idea = get_object_or_404(Idea, id=idea_id)
    idea.delete()
    return redirect('ideas:list_of_ideas', campaign_id)

@login_required
def idea_update(request, idea_id, campaign_id):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    comments = Comment.objects.all().filter(idea_id=idea_id)
    idea = Idea.objects.get(id=idea_id)
    form = IdeaForm(request.POST if request.POST else None, instance=idea)
    field = form.fields['campaign_id']
    field.widget = field.hidden_widget()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return render(request, 'ideas/idea_details.html', {'idea': idea, 'campaign': campaign, 'comments': comments})
    return render(request, 'ideas/idea_update.html', {'form': form})

@login_required
def idea_like(request, campaign_id, idea_id):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    user = request.user
    idea = Idea.objects.get(id=idea_id)
    comments = Comment.objects.all().filter(idea_id=idea_id)
    if request.method == 'POST':
        if user in idea.idea_likes.all():
            idea.idea_likes.remove(user)
        else:
            idea.idea_likes.add(user)
        like, created = IdeaLike.objects.get_or_create(
            user=user, idea_id=idea_id)
        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
        like.save()
    previous_url = request.META.get('HTTP_REFERER')
    if 'ideas' in previous_url:
        return render(request, 'ideas/idea_details.html', {'idea': idea, 'campaign': campaign, 'comments': comments})
    else:
        return redirect('campaigns:campaign_details', campaign_id=campaign_id)
    
@login_required
def add_favorite_idea(request, campaign_id, idea_id):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    idea = get_object_or_404(Idea, pk=idea_id)
    idea.idea_favorites.add(request.user)
    comments = Comment.objects.all().filter(idea_id=idea_id)
    return render(request, 'ideas/idea_details.html', {'idea': idea, 'campaign': campaign, 'comments': comments})

@login_required
def remove_favorite_idea(request, campaign_id, idea_id):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    idea = get_object_or_404(Idea, pk=idea_id)
    idea.idea_favorites.remove(request.user)
    comments = Comment.objects.all().filter(idea_id=idea_id)
    return render(request, 'ideas/idea_details.html', {'idea': idea, 'campaign': campaign, 'comments': comments})
