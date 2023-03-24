from django_codenerix.db import models, Q
from django_codenerix import definitions, lists
from django_codeneris.forms import widgets

from propoll.definitions.author import Author


class Question(definitions.Codefine):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    class Meta:
        admin = True
        show_details = True
        default_ordering = "-question_text"
        extra_context = "???"
        linkadd = "maybe should be an 'allow_add'"
        linkedit = "maybe should be an 'allow_edit'"
        linkdelete = "maybe should be an 'allow_delete'"

    def save(self):
        print(self.pk)
        return super().save()

    class List:
        pk = None
        question_text = None
        pub_date = None

        class Search:
            def general_box_search(self, text):
                return Q(question_text=text)

            __main__ = general_box_search
            question_text = lists.SearchField(
                "Pregunta",
                lambda x: Q(level_study__pk=x),
                choices=[(obj.pk, obj.name) for obj in Author.objects.all()],
            )

    class Form:
        """
        Somehow they must support field linking for autofill
        Autofill must be static (with preloaded data or dynamic with dynamic loading) - We must think about this anyway maybe all can be dynamic
        When writting in an autofill the software should undetand that the text written is used only for search (this may happen in one field or in a mix of several fields, an algorithm should be allowed to respond to the autofill as well like you can do in Codenerix-Legacy)
        """

        class Group1:
            # Usage of ellipsis is also allowed
            question_text = widgets.Any(...)
            pub_date = widgets.Any

            class Meta:
                default_widget = widgets.Any(2)

        class Meta:
            default_widget = widgets.Any(3)

        class AutoFill:
            """
            I don't get convinced by this definition
            Autofill must know about the fields that will be queried from the model and the fields that will be filled once requested:
            - if I write in an autofill the text wrotten will be sent and the remote service, function of whatever must understand about the search (we must be able to send linkend filters as well)
            """

            question_text = widgets.Autofill("Details", 3)

            def dynfield(dynamic_answer):
                pass

            question_text = widgets.Autofill(dynfield)

            question_text = widgets.Autofill(
                url="/custom/url", linked_fields=["field1", "field2", "field3"]
            )

    class Details:
        class Group1:
            question_text = widgets.Any(6)

        class Group2:
            pub_date = widgets.Any(6)
