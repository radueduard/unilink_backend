import uuid

from django.db import models
from ..Models.grupa import Grupa


class Semigrupa(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nume = models.CharField(max_length=1, default='')
    grupa = models.ForeignKey(Grupa, related_name='semigrupe', on_delete=models.CASCADE, default='')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.grupa.__str__() + " " + self.nume + " " + self.id.__str__()
