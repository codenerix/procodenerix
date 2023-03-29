from rest_framework import serializers
from django.utils.translation import gettext as _

from django_codenerix.info_model import InfoModel
from .info.choice import Choice


class Question(InfoModel):
    class Serializer(object):
        choices = serializers.PrimaryKeyRelatedField(many=True, queryset=Choice.meta.info.queryset_serializer())

    @staticmethod
    def serializer_fields():
        return ['question_text', 'pub_date', 'choices']

    @staticmethod
    def queryset():
        return Choice.objects.all()

    def __fields__(self, info):
        fields = []
        fields.append(('question', _('Question')))
        fields.append(('choice_text', _('Choice Text')))
        fields.append(('votes', _('Votes')))

        return fields

    def __str__(self):
        return '{}'.format(self.choice_text)

    def __form__(self, info):
        group = [
            (
                _('Details', 12),
                ['question', 3],
                ['choice_text', 6],
                ['votes', 3],
            )
        ]
        return group
