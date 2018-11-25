# coding: utf-8
from django.urls import path
from .views import NamesView


urlpatterns = [
    path('names/', NamesView.as_view()),
]
