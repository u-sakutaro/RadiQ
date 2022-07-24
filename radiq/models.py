from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# 投稿のDB作成
class Post(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE) #many_to_one(たくさん投稿できるように)
    date_posted = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.content

# 返信のDB作成 
class Comment(models.Model):
    comment = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    target = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='回答相手')
    date_posted = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.comment[:20]