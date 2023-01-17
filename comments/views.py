from django.shortcuts import render
from .forms import CommentForm
from .models import Comment
from django.shortcuts import get_object_or_404, redirect

def list_of_comments(request, idea_id, campaign_id):
    comments = Comment.objects.all().filter(idea_id=idea_id)
    context = {'comments': comments}
    return render(request, 'comments/comments_list.html', context)

def comment_details(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    
    if request.method == 'GET':
        form = CommentForm(instance=comment)
        context =  {'form': form, 'comment': comment}
        return render(request, 'comments/comment_details.html', context)
    else:
        try:
            form = CommentForm(request.POST, instance=commnet)
            form.save()
            return redirect('comments:list_of_comments')
        except ValueError:
            context = {'form': CommentForm(), 'error': 'Bad data try again'}
            return render(request, 'comments/comment_details.html', context)
    

def comment_create(request):
    if request.method == 'GET':
        return render(request, 'comments/comment_form.html', {'form': CommentForm()})
    else:
        try:
            form = CommentForm(request.POST)
            form.save()
            return redirect('comments:list_of_comments')
        except ValueError:
            context = {'form': CommentForm(), 'error': 'Bad data try again'}
            return render(request, 'comments/comment_form.html', context)
        
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return redirect('comments:list_of_comments')

def comment_update(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    form = CommentForm(instance=comment)
    return render(request, 'comments/comment_update.html', {'form': form})

