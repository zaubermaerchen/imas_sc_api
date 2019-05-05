from django.db import models


class Character(models.Model):
    name = models.CharField(max_length=255, primary_key=True)

    class Meta:
        db_table = 'character'
