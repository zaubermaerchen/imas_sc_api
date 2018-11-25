# coding: utf-8
from rest_framework import serializers
from data.models import Cartoon


class SearchSerializer(serializers.ModelSerializer):
    characters = serializers.SerializerMethodField(read_only=True)
    thumbnail_hash = serializers.SerializerMethodField(read_only=True)
    image_hash = serializers.SerializerMethodField(read_only=True)
    tweet_id = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Cartoon
        fields = [
            'id',
            'type',
            'episode',
            'title',
            'release_date',
            'characters',
            'thumbnail_hash',
            'image_hash',
            'tweet_id'
        ]

    @staticmethod
    def get_thumbnail_hash(obj):
        return obj.thumbnail_hash if len(obj.thumbnail_hash) > 0 else None

    @staticmethod
    def get_image_hash(obj):
        return obj.image_hash if len(obj.image_hash) > 0 else None

    @staticmethod
    def get_tweet_id(obj):
        return str(obj.tweet_id) if obj.tweet_id > 0 else None

    @staticmethod
    def get_characters(obj):
        return obj.characters.split()
