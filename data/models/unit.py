from django.db import models


class Unit(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'unit'
        ordering = ['id']

    def __str__(self):
        return self.name
