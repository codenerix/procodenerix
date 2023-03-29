from rest_framework import serializers

from .models import Choice


class ChoiceSerializer(serializers.HyperlinkedModelSerializer, Choice.meta.info.Serializer):
    class Meta:
        model = Choice
        fields = Choice.meta.info.serializer_fields
