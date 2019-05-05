# -*- coding: utf-8 -*-
from django.contrib import admin


class IdolAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'unit',
    )


