import uuid

from django.db import models


class Facultate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    num = models.IntegerField(default=0)
    name = models.CharField(max_length=100, default='')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
