import uuid
from enum import Enum
from django.db import models
from .materie import Materie, Curs, Laborator, Seminar
from .sala import Sala


class Day(Enum):
    MON = 0
    TUE = 1
    WEN = 2
    THU = 3
    FRI = 4
    ERR = 5


class Week(Enum):
    EVEN = 0
    ODD = 1
    BOTH = 2
    ERR = 3


class Schedule(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    week = models.IntegerField(default=Week.ERR)
    day = models.IntegerField(default=Day.ERR)
    sala = models.ForeignKey(Sala, related_name="schedules", on_delete=models.SET_NULL, default=0, null=True)
    startingHour = models.IntegerField(default=0)


class ScheduleC(Schedule):
    curs = models.ForeignKey(Curs, related_name='schedules', on_delete=models.SET_NULL, default=0, null=True)


class ScheduleS(Schedule):
    seminar = models.ForeignKey(Seminar, related_name='schedules', on_delete=models.SET_NULL, default=0, null=True)


class ScheduleL(Schedule):
    laborator = models.ForeignKey(Laborator, related_name='schedules', on_delete=models.SET_NULL, default=0, null=True)
