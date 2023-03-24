# from django.test import TestCase
from pytest import mark
from django.utils import timezone
from polls.models import Choice, Question


def test_base():
    assert 1 == 1


@mark.django_db
def test_choice():
    qtext = "What's new?"
    q = Question(question_text=qtext, pub_date=timezone.now())
    q.save()

    qs = Question.objects.filter(question_text=qtext).all()
    assert len(qs) == 1
    assert qs[0].question_text == qtext
