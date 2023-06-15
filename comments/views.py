from django.shortcuts import render
from .forms import CommentForm
from .models import Comment, CommentLike
from django.shortcuts import get_object_or_404, redirect
from ideas.models import Idea
import re
from django.db.models import Count
from django.contrib.auth.decorators import login_required


def list_of_comments(request, idea_id, campaign_id):
    comments = Comment.objects.all().order_by('-created_at')
    context = {'comments': comments}
    return render(request, 'ideas/idea_details.html', context)


def list_of_top_comments(request, idea_id, campaign_id):
    top_comments = Comment.objects.annotate(
        q_count=Count('likes')).order_by('-q_count')[:7]
    context = {'comments': top_comments}
    return render(request, 'ideas/idea_details.html', context)


def comment_details(request, comment_id, idea_id, campaign_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.method == 'GET':
        form = CommentForm(instance=comment)
        context = {'form': form, 'comment': comment,
                   'idea_id': idea_id, 'campaign_id': campaign_id}
        return render(request, 'comments/comment_details.html', context)
    else:
        try:
            form = CommentForm(request.POST, instance=comment)
            form.save()
            return redirect('comments:list_of_comments', idea_id, campaign_id)
        except ValueError:
            context = {'form': CommentForm(), 'error': 'Bad data try again'}
            return render(request, 'comments/comment_details.html', context)

@login_required
def comment_create(request, idea_id, campaign_id, comment_id=0):
    if comment_id is 0:
        if request.method == 'GET':
            form = CommentForm(initial={'idea_id': idea_id})
            field = form.fields['idea_id']
            field.widget = field.hidden_widget()

            return render(request, 'comments/comment_form.html', {'form': form})
        else:
            try:
                form = CommentForm(request.POST, request.FILES,
                                   initial={'idea_id': idea_id})
                form.save()
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
                form = CommentForm(request.POST, request.FILES,
                                   initial={'idea_id': idea_id, 'comment_id': comment_id})
                comment = form.save(commit=False)
                comment.parent = parent_comment
                field = form.fields['idea_id']
                field.widget = field.hidden_widget()
                field = form.fields['comment_id']
                field.widget = field.hidden_widget()
                form.save()
                return redirect('idea_details', campaign_id, idea_id)
            except ValueError:
                context = {'form': CommentForm(
                ), 'error': 'Bad data try again'}
                return render(request, 'comments/comment_form.html', context)

@login_required
def comment_delete(request, comment_id, idea_id, campaign_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return redirect('idea_details', campaign_id, idea_id)

@login_required
def comment_update(request, comment_id, idea_id, campaign_id):
    comment = Comment.objects.get(id=comment_id)
    form = CommentForm(
        request.POST if request.POST else None, instance=comment)
    field = form.fields['idea_id']
    field.widget = field.hidden_widget()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect('idea_details', campaign_id, idea_id)
    return render(request, 'comments/comment_update.html', {'form': form})

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
