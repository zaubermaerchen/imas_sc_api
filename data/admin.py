# -*- coding: utf-8 -*-
from django.contrib import admin
from data.models import Cartoon


class CartoonAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'type',
        'episode',
        'title',
        'release_date',
        'characters',
        'comment',
    )
    fieldsets = [
        (None, {
            'fields': [
                'id',
                'type',
                'episode',
                'title',
                'release_date',
                'characters',
                'thumbnail_hash',
                'image_hash',
                'tweet_id',
                'comment'
            ]
        })
    ]
    search_fields = ['title']


admin.site.register(Cartoon, CartoonAdmin)
