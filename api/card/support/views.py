# coding: utf-8
from rest_framework import generics
from .serializer import ListSerializer
from .pagination import ListLimitOffsetPagination
from data.models.support_card import SupportCard


class SearchView(generics.ListAPIView):
    serializer_class = ListSerializer
    pagination_class = ListLimitOffsetPagination

    def get_queryset(self):
        # リクエストから必要なパラメータを取得
        idol_id_list = self.request.query_params.getlist('idol_id')
        rarity_list = self.request.query_params.getlist('rarity')

        return SupportCard.get_list(idol_id_list, rarity_list)
