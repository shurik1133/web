from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')

    def popular(self):
        return self.order_by('-rating')


class Question(models.Model):
    object = QuestionManager

    title = models.CharField(max_length=255)
    text = models.TextField(default='', null=False)
    added_at = models.DateTimeField()
    rating = models.IntegerField(default=0, null=False)
    author = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='question_likes_set')


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField()
    question = models.ForeignKey(Question, null=False, on_delete=models.CASCADE)
    author = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
