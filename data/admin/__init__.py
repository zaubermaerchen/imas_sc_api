# -*- coding: utf-8 -*-
from django.contrib import admin
from data.models.unit import Unit
from data.models.idol import Idol
from data.models.produce_card import ProduceCard
from data.models.support_card import SupportCard
from data.models.cartoon import Cartoon
from data.admin.unit import UnitAdmin
from data.admin.idol import IdolAdmin
from data.admin.produce_card import ProduceCardAdmin
from data.admin.support_card import SupportCardAdmin
from data.admin.cartoon import CartoonAdmin

admin.site.register(Unit, UnitAdmin)
admin.site.register(Idol, IdolAdmin)
admin.site.register(ProduceCard, ProduceCardAdmin)
admin.site.register(SupportCard, SupportCardAdmin)
admin.site.register(Cartoon, CartoonAdmin)
