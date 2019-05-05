# coding: utf-8
from rest_framework import serializers
from data.models.idol import Idol


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idol
        fields = ['id', 'name']
