# coding: utf-8
from django.urls import path
from .views import ListView


urlpatterns = [
    path('list/', ListView.as_view()),
]
