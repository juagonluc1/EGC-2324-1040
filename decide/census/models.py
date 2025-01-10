from django.db import models


class Census(models.Model):
    voting_id = models.PositiveIntegerField()
    voter_id = models.PositiveIntegerField()
    t2="Este es otro texto"

    class Meta:
        unique_together = (('voting_id', 'voter_id',t2),)
