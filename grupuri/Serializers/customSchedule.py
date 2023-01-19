from rest_framework import serializers
from ..Models.customSchedule import CustomInclusion, CustomExclusion


class InclusionSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomInclusion
        fields = ['id', 'schedule', 'student']


class ExclusionSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomExclusion
        fields = ['id', 'schedule', 'student']
