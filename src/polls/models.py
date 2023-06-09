from django.db import 
from django_codenerix.models import CodenerixModel
from .info.question import Question
from .info.choice import Choice


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    class Meta(CodenerixModel.Meta):
        codenerix_meta = Question


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    class Meta(CodenerixModel.Meta):
        codenerix_meta = Choice
