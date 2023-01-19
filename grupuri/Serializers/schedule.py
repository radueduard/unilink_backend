from rest_framework import serializers

from .materie import CursSerializer, LaboratorSerializer, SeminarSerializer, CursSerializerGET, SeminarSerializerGET, \
    LaboratorSerializerGET
from .sala import SalaSerializer
from ..Models.schedule import Schedule, ScheduleC, ScheduleS, ScheduleL


class ScheduleSerializer(serializers.ModelSerializer):
    sala = SalaSerializer(many=False, read_only=True)

    class Meta:
        model = Schedule
        fields = ['id', 'week', 'day', 'sala', 'startingHour']


class ScheduleCSerializer(ScheduleSerializer):
    curs = CursSerializerGET(many=False, read_only=True)

    class Meta(ScheduleSerializer.Meta):
        model = ScheduleC
        fields = ScheduleSerializer.Meta.fields + ['curs']


class ScheduleSSerializer(ScheduleSerializer):
    seminar = SeminarSerializerGET(many=False, read_only=True)

    class Meta(ScheduleSerializer.Meta):
        model = ScheduleS
        fields = ScheduleSerializer.Meta.fields + ['seminar']


class ScheduleLSerializer(ScheduleSerializer):
    laborator = LaboratorSerializerGET(many=False, read_only=True)

    class Meta(ScheduleSerializer.Meta):
        model = ScheduleL
        fields = ScheduleSerializer.Meta.fields + ['laborator']
