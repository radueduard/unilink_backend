from rest_framework import serializers

from .grupa import GrupaSerializer
from ..Models.serie import Serie


class SerieSerializerComplete(serializers.ModelSerializer):
    grupe = GrupaSerializer(many=True, read_only=True)

    class Meta:
        model = Serie
        fields = ['id', 'nume', 'an', 'grupe']


class SerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serie
        fields = ['id', 'nume', 'an', 'created', 'updated']
