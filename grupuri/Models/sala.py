import uuid

from django.db import models


class Sala(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cladire = models.CharField(default="Invalid Building...", max_length=3)
    num = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Sala " + self.cladire.__str__() + self.num.__str__() + ' ' + self.id.__str__()
