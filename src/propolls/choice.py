from django.db import models, Count
from django_codenerix import definitions
from django_codeneris.forms import widgets
from propolls.question import Question


class Choice(definitions.Codefine):
    name = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question_counts = models.Annotation("name", Count)

    class Admin:
        admin = True

    class Form:
        class Meta:
            include = []
            exclude = []

        class Group1:
            question = widgets.Any(3, "Pregunta")
            choice_text = widgets.Any(3, "Eleccion")

        class Group2:
            votes: widgets.Any(6)

    class Details(Form):
        pass
