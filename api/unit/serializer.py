# coding: utf-8
from rest_framework import serializers
from data.models.unit import Unit


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ['id', 'name']
