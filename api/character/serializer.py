# coding: utf-8
from rest_framework import serializers
from data.models.character import Character


class NamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['name']
