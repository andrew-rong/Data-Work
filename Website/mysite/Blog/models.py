from django.db import models
import datetime
from django.contrib.auth.models import User


class Post(models.Model):
    post_text = models.TextField()
    thoughts = models.TextField(default=None, null=True)
    pub_date = models.DateTimeField('date published')
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.post_text


class Choice(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
