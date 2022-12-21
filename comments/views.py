from django.shortcuts import render
from .models import Comment
# Create your views here.

def list_of_commentss(request):
    comments = Comment.objects.all()
    context = {'comments': comments}
    return render(request, 'comments/home.html', context)

def comment_details(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    context = {'comment': comment}
    return render(request, 'comments/comment_details.html', context)