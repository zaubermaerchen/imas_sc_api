# coding: utf-8
from rest_framework import serializers
from data.models.support_card import SupportCard


class ListSerializer(serializers.ModelSerializer):
    icon_hash = serializers.SerializerMethodField(read_only=True)
    card_hash = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = SupportCard
        fields = [
            'id',
            'name',
            'rarity',
            'idol_id',
            'release_date',
            'icon_hash',
            'card_hash',
            'vocal',
            'dance',
            'visual',
            'mental',
            'max_vocal',
            'max_dance',
            'max_visual',
            'max_mental',
            'idea',
        ]

    @staticmethod
    def get_icon_hash(obj):
        return obj.icon_hash if len(obj.icon_hash) > 0 else None

    @staticmethod
    def get_card_hash(obj):
        return obj.card_hash if len(obj.card_hash) > 0 else None
