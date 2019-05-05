# -*- coding: utf-8 -*-
from django.contrib import admin


class SupportCardAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'rarity',
        'idol',
        'release_date',
    )
    fieldsets = [
        (None, {
            'fields': [
                'name',
                'rarity',
                'idol',
                'release_date',
                'idea',
            ]
        }),
        ('Status', {
            'fields': [
                'vocal',
                'dance',
                'visual',
                'mental',
                'max_vocal',
                'max_dance',
                'max_visual',
                'max_mental',
            ]
        }),
        ('Hash', {
            'fields': [
                'icon_hash',
                'card_hash',
            ]
        }),
    ]
    search_fields = ['name']
