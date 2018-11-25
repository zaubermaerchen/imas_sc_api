# coding: utf-8
from rest_framework import generics
from datetime import datetime
from .serializer import SearchSerializer
from .pagination import SearchLimitOffsetPagination
from data.models import Cartoon


def convert_datetime_object(datetime_string, datetime_format):
    if datetime_string is None or len(datetime_string) == 0:
        return None

    value = None
    try:
        value = datetime.strptime(datetime_string, datetime_format)
    finally:
        return value


class SearchView(generics.ListAPIView):
    serializer_class = SearchSerializer
    pagination_class = SearchLimitOffsetPagination

    def get_queryset(self):
        # リクエストから必要なパラメータを取得
        title = self.request.query_params.get('title')
        characters = self.request.query_params.getlist('character')
        start_at = convert_datetime_object(self.request.query_params.get('start_at'), '%Y-%m-%d')
        end_at = convert_datetime_object(self.request.query_params.get('end_at'), '%Y-%m-%d')

        return Cartoon.get_list(title, characters, start_at, end_at)
