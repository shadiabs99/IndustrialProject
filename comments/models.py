from django.db import models
from participants.models import Participant
from ideas.models import Idea
from author.decorators import with_author
from django.contrib.auth.models import User

@with_author
class Comment(models.Model):
    content = models.TextField(max_length=250)
    idea_id = models.IntegerField(null=True)
    
    likes = models.ManyToManyField(User, default=None, blank=True, related_name="comment_likes")

    def __str__(self):
        return self.content
    
    @property
    def num_likes(self):
        return self.likes.all().count()
    
LIKE_CHOICES = (
    ('Like', 'Like'), 
    ('Unlike', 'Unlike')
)

class CommentLike (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)
    
    def __str__(self):
        return str(self.comment)