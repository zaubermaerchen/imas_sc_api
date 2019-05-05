# coding: utf-8
from rest_framework import serializers
from data.models.produce_card import ProduceCard


class ListSerializer(serializers.ModelSerializer):
    icon_hash = serializers.SerializerMethodField(read_only=True)
    card_hash = serializers.SerializerMethodField(read_only=True)
    fes_card_hash = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = ProduceCard
        fields = [
            'id',
            'name',
            'rarity',
            'idol_id',
            'release_date',
            'icon_hash',
            'card_hash',
            'fes_card_hash'
        ]

    @staticmethod
    def get_icon_hash(obj):
        return obj.icon_hash if len(obj.icon_hash) > 0 else None

    @staticmethod
    def get_card_hash(obj):
        return obj.card_hash if len(obj.card_hash) > 0 else None

    @staticmethod
    def get_fes_card_hash(obj):
        return obj.fes_card_hash if len(obj.fes_card_hash) > 0 else None
