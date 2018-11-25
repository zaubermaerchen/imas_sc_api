# coding: utf-8
from rest_framework.pagination import LimitOffsetPagination


class SearchLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100
