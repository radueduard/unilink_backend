import uuid

from django.db import models
from .facultate import Facultate


class An(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    num = models.IntegerField(default=0)
    facultate = models.ForeignKey(Facultate, related_name='ani', on_delete=models.CASCADE, default=0)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Anul " + self.num.__str__() + ", " + self.facultate.__str__()
