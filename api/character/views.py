# coding: utf-8
from rest_framework import generics
from .serializer import NamesSerializer
from data.models.character import Character


class NamesView(generics.ListAPIView):
    serializer_class = NamesSerializer
    queryset = Character.objects.all()

