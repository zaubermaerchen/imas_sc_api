# coding: utf-8
from rest_framework import generics
from .serializer import ListSerializer
from data.models.idol import Idol


class ListView(generics.ListAPIView):
    serializer_class = ListSerializer
    queryset = Idol.objects.all()

