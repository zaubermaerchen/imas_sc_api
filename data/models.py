from django.db import models


class Character(models.Model):
    name = models.CharField(max_length=255, primary_key=True)

    class Meta:
        db_table = 'character'


class Cartoon(models.Model):
    TYPE_CHOICES = (
        (0, '通常'),
        (1, '特別'),
        (2, '限定'),
    )

    id = models.IntegerField(primary_key=True)
    type = models.IntegerField(choices=TYPE_CHOICES, default=0)
    episode = models.IntegerField(default=0)
    title = models.CharField(max_length=256, default='')
    release_date = models.DateField(default='0000-00-00')
    characters = models.TextField(blank=True)
    thumbnail_hash = models.CharField(max_length=64, blank=True, default='')
    image_hash = models.CharField(max_length=64, blank=True, default='')
    tweet_id = models.BigIntegerField(default=0)
    comment = models.CharField(max_length=256, blank=True, default='')

    class Meta:
        db_table = 'cartoon'
        ordering = ['id']

    @classmethod
    def get_list(cls, title=None, characters=None, start_at=None, end_at=None):
        cartoons = cls.objects.all()

        if title is not None and len(title) > 0:
            where = 'MATCH(title) AGAINST (%s IN BOOLEAN MODE)'
            param = '*D+ ' + title
            cartoons = cartoons.extra(where=[where], params=[param])

        if characters is not None and len(characters) > 0:
            where = 'MATCH(characters) AGAINST (%s IN BOOLEAN MODE)'
            param = '+' + ' +'.join(characters)
            cartoons = cartoons.extra(where=[where], params=[param])

        if start_at is not None:
            cartoons = cartoons.filter(release_date__gte=start_at)

        if end_at is not None:
            cartoons = cartoons.filter(release_date__lte=end_at)

        return cartoons
