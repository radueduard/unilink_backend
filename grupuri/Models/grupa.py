import uuid

from django.db import models
from ..Models.serie import Serie


class Grupa(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    num = models.IntegerField(default=0)
    serie = models.ForeignKey(Serie, related_name='grupe', on_delete=models.CASCADE, default='')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Grupa " + self.num.__str__() + " " + self.serie.__str__()

