# coding: utf-8
from django.urls import path, include


urlpatterns = [
    path('produce/', include('api.card.produce.urls')),
    path('support/', include('api.card.support.urls')),
]
