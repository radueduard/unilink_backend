from django.utils import timezone
from django.db import models
from .materie import Curs
import uuid


def one_week_view():
    return timezone.now() + timezone.timedelta(days=7)

class Tema(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    curs = models.ForeignKey(Curs, related_name='teme', on_delete=models.CASCADE, default='')
    title = models.CharField(max_length=100, default='Invalid title')
    description = models.TextField(null=True, blank=True, default='Invalid description')
    due_date = models.DateTimeField(default=one_week_view)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title.__str__() + ' due on ' + self.due_date.__str__()


class Examen(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    curs = models.ForeignKey(Curs, related_name='examene', on_delete=models.CASCADE, default='')
    title = models.CharField(max_length=100, default='Invalid title')
    description = models.TextField(null=True, blank=True, default='Invalid description')
    tip = models.CharField(max_length=20, default='examen')
    date = models.DateTimeField(default=one_week_view)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title.__str__() + ', date: ' + self.date.__str__()
