# -*- coding: utf-8 -*-
from django.contrib import admin


class ProduceCardAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'rarity',
        'idol',
    )
    fieldsets = [
        (None, {
            'fields': [
                'name',
                'rarity',
                'idol',
                'release_date',
            ]
        }),
        ('Hash', {
            'fields': [
                'icon_hash',
                'card_hash',
                'fes_card_hash',
            ]
        }),
    ]
    search_fields = ['name']
