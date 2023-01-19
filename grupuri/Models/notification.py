import uuid

from django.db import models

from .materie import Curs, Seminar, Laborator


class NotificationSchedule(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mesaj = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mesaj.__str__()


class NotificationCourse(NotificationSchedule):
    sender = models.ForeignKey(Curs, related_name='notificari', on_delete=models.CASCADE)

    def __str__(self):
        return self.mesaj.__str__()


class NotificationSeminar(NotificationSchedule):
    sender = models.ForeignKey(Seminar, related_name='notificari', on_delete=models.CASCADE)

    def __str__(self):
        return self.mesaj.__str__()


class NotificationLab(NotificationSchedule):
    sender = models.ForeignKey(Laborator, related_name='notificari', on_delete=models.CASCADE)

    def __str__(self):
        return self.mesaj.__str__()
