from django.db import models


class Census(models.Model):
    voting_id = models.PositiveIntegerField()
    voter_id = models.PositiveIntegerField()
    texto1="Este es un texto"

    class Meta:
        unique_together = (('voting_id', 'voter_id',texto1),)
