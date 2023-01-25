from django.shortcuts import render
from .forms import CommentForm
from .models import Comment, CommentLike
from django.shortcuts import get_object_or_404, redirect
from ideas.models import Idea
import re


def list_of_comments(request, idea_id, campaign_id):
    comments = Comment.objects.all().filter(idea_id=idea_id)
    context = {'comments': comments}
    return render(request, 'ideas/idea_details.html', context)


def list_of_top_comments(request):
    top_comments = Comment.objects.annotate(
        q_count=Count('likes')).order_by('-q_count')[:7]
    context = {'comments': top_comments}
    return render(request, 'ideas/idea_details.html', context)


def comment_details(request, comment_id, idea_id, campaign_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.method == 'GET':
        form = CommentForm(instance=comment)
        context = {'form': form, 'comment': comment, 'idea_id': idea_id}
        return render(request, 'comments/comment_details.html', context)
    else:
        try:
            form = CommentForm(request.POST, instance=comment)
            form.save()
            return redirect('comments:list_of_comments', idea_id, campaign_id)
        except ValueError:
            context = {'form': CommentForm(), 'error': 'Bad data try again'}
            return render(request, 'comments/comment_details.html', context)


def comment_create(request, idea_id, campaign_id):
    user = request.user

    if request.method == 'GET':
        form = CommentForm(initial={'idea_id': idea_id})
        return render(request, 'comments/comment_form.html', {'form': form})
    else:
        try:
            form = CommentForm(request.POST, request.FILES,
                               initial={'idea_id': idea_id})
            form.save()
            return redirect('idea_details', campaign_id, idea_id)
        except ValueError:
            context = {'form': CommentForm(), 'error': 'Bad data try again'}
            return render(request, 'comments/comment_form.html', context)


def comment_delete(request, comment_id, idea_id, campaign_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return redirect('idea_details', campaign_id, idea_id)


def comment_update(request, comment_id, idea_id, campaign_id):
    comment = Comment.objects.get(id=comment_id)
    form = CommentForm(
        request.POST if request.POST else None, instance=comment)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect('idea_details', campaign_id, idea_id)
    return render(request, 'comments/comment_update.html', {'form': form})


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
