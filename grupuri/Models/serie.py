import uuid

from django.db import models
from .an import An


class Serie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nume = models.CharField(max_length=5, default='')
    an = models.ForeignKey(An, related_name="serii", on_delete=models.CASCADE, default=0)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Seria " + self.nume.__str__() + ", " + self.an.__str__()
