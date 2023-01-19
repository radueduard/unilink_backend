from rest_framework import serializers

from .materie import SeminarSerializerGET, CursSerializerGET, LaboratorSerializerGET
from ..Models.notification import NotificationSchedule, NotificationSeminar, NotificationCourse, NotificationLab


class NotificationScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationSchedule
        fields = ['id', 'mesaj']


class NotificationCourseSerializer(NotificationScheduleSerializer):
    sender = CursSerializerGET(many=False, read_only=True)

    class Meta(NotificationScheduleSerializer.Meta):
        model = NotificationCourse
        fields = NotificationScheduleSerializer.Meta.fields + ['sender']


class NotificationCourseSerializerPOST(NotificationScheduleSerializer):
    class Meta(NotificationScheduleSerializer.Meta):
        model = NotificationCourse
        fields = NotificationScheduleSerializer.Meta.fields + ['sender']


class NotificationSeminarSerializer(NotificationScheduleSerializer):
    sender = SeminarSerializerGET(many=False, read_only=True)

    class Meta(NotificationScheduleSerializer.Meta):
        model = NotificationSeminar
        fields = NotificationScheduleSerializer.Meta.fields + ['sender']


class NotificationLabSerializer(NotificationScheduleSerializer):
    sender = LaboratorSerializerGET(many=False, read_only=True)

    class Meta(NotificationScheduleSerializer.Meta):
        model = NotificationLab
        fields = NotificationScheduleSerializer.Meta.fields + ['sender']