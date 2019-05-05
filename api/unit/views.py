# coding: utf-8
from rest_framework import generics
from .serializer import ListSerializer
from data.models.unit import Unit


class ListView(generics.ListAPIView):
    serializer_class = ListSerializer
    queryset = Unit.objects.all()

