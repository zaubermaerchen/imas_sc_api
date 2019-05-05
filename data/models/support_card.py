from django.db import models
from django.utils import timezone
from data.models.idol import Idol


class SupportCard(models.Model):
    RARITY_CHOICES = (
        (1, 'N'),
        (2, 'R'),
        (3, 'SR'),
        (4, 'SSR'),
    )
    IDEA_CHOICES = (
        (1, 'ボーカル'),
        (2, 'ダンス'),
        (3, 'ビジュアル'),
        (4, 'トーク'),
        (5, 'アピール'),
    )

    name = models.CharField(max_length=255)
    rarity = models.IntegerField(choices=RARITY_CHOICES, default=1)
    idol = models.ForeignKey(Idol, default=1, on_delete=models.PROTECT)
    release_date = models.DateField(default=timezone.now)
    icon_hash = models.CharField(max_length=64, blank=True, default='')
    card_hash = models.CharField(max_length=64, blank=True, default='')
    vocal = models.IntegerField(default=0)
    dance = models.IntegerField(default=0)
    visual = models.IntegerField(default=0)
    mental = models.IntegerField(default=0)
    max_vocal = models.IntegerField(default=0)
    max_dance = models.IntegerField(default=0)
    max_visual = models.IntegerField(default=0)
    max_mental = models.IntegerField(default=0)
    idea = models.IntegerField(choices=IDEA_CHOICES, default=1)

    class Meta:
        db_table = 'support_card'
        ordering = ['-rarity', 'idol', 'release_date']

    @classmethod
    def get_list(cls, idol_id_list=None, rarity_list=None):
        card_list = cls.objects.all()

        if idol_id_list is not None and len(idol_id_list) > 0:
            card_list = card_list.filter(idol_id__in=idol_id_list)

        if rarity_list is not None and len(rarity_list) > 0:
            card_list = card_list.filter(rarity__in=rarity_list)

        return card_list
