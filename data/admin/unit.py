# -*- coding: utf-8 -*-
from django.contrib import admin


class UnitAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )
