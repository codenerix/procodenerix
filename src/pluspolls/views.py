from rest_framework import generics

from .models import Choice
from .serializer import ChoiceSerializer


class ChoiceList(generics.ListCreateAPIView):
    queryset = Choice.meta.info.queryset()
    serializer_class = ChoiceSerializer


class ChoiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Choice.meta.info.queryset()
    serializer_class = ChoiceSerializer
