from django.utils.translation import gettext as _

from django_codenerix.info_model import InfoModel


class Choice(InfoModel):
    @staticmethod
    def serializer_fields():
        return ['question', 'choice_text', 'votes']

    @staticmethod
    def queryset():
        return Choice.objects.all()

    @staticmethod
    def queryset_serializer():
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
