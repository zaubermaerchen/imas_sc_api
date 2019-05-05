from django.db import models
from data.models.unit import Unit


class Idol(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    unit = models.ForeignKey(Unit, default=1, on_delete=models.PROTECT)

    class Meta:
        db_table = 'idol'
        ordering = ['id']

    def __str__(self):
        return self.name
