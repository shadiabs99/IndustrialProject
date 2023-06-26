from django.shortcuts import render
from .forms import CommentForm
from .models import Comment, CommentLike
from django.shortcuts import get_object_or_404, redirect
from ideas.models import Idea
from campaigns.models import Campaign
from profiles.models import Profile
import re
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from IntelInnovation.common import Score

@login_required
def comment_create(request, idea_id, campaign_id, comment_id=0):
    user = request.user
    profile = Profile.objects.get(user_id=user.id)
    if comment_id == 0:
        if request.method == 'GET':
            form = CommentForm(initial={'idea_id': idea_id})
            field = form.fields['idea_id']
            field.widget = field.hidden_widget()

            return render(request, 'comments/comment_form.html', {'form': form})
        else:
            try:
                profile.score = profile.score + Score.NEW_COMMENT.value
                form = CommentForm(request.POST, request.FILES,
                                   initial={'idea_id': idea_id})
                form.save()
                profile.save()
                return redirect('idea_details', campaign_id, idea_id)
            except ValueError:
                context = {'form': CommentForm(
                ), 'error': 'Bad data try again'}
                return render(request, 'comments/comment_form.html', context)
    else:
        parent_comment = get_object_or_404(Comment, id=comment_id)
        if request.method == 'GET':
            form = CommentForm(
                initial={'idea_id': idea_id, 'comment_id': comment_id})
            comment = form.save(commit=False)
            comment.parent = parent_comment
            field = form.fields['idea_id']
            field.widget = field.hidden_widget()
            field = form.fields['comment_id']
            field.widget = field.hidden_widget()
            return render(request, 'comments/comment_form.html', {'form': form})
        else:
            try:
                profile.score = profile.score + Score.NEW_COMMENT.value
                form = CommentForm(request.POST, request.FILES,
                                   initial={'idea_id': idea_id, 'comment_id': comment_id})
                comment = form.save(commit=False)
                comment.parent = parent_comment
                field = form.fields['idea_id']
                field.widget = field.hidden_widget()
                field = form.fields['comment_id']
                field.widget = field.hidden_widget()
                form.save()
                profile.save()
                return redirect('idea_details', campaign_id, idea_id)
            except ValueError:
                context = {'form': CommentForm(
                ), 'error': 'Bad data try again'}
                return render(request, 'comments/comment_form.html', context)

@login_required
def comment_like(request, comment_id, idea_id, campaign_id):
    user = request.user
    if request.method == 'POST':

        comment = Comment.objects.get(id=comment_id)

        if user in comment.likes.all():
            comment.likes.remove(user)
        else:
            comment.likes.add(user)
        like, created = CommentLike.objects.get_or_create(
            user=user, comment_id=comment_id)
        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
        like.save()
    return redirect('idea_details', campaign_id, idea_id)


def top_comments(request, idea_id, campaign_id):
    campaign = get_object_or_404(Campaign, id=campaign_id)
    idea = get_object_or_404(Idea, id=idea_id)
    comments = Comment.objects.all().filter(idea_id=idea_id).annotate(q_count=Count('likes')).order_by('-q_count')[:7]
    context = { 'campaign': campaign, 'comments': comments, 'idea': idea}
    return render(request, 'ideas/idea_details.html', context)