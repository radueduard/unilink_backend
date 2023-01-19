from rest_framework import serializers
from ..Models.an import An
from ..Serializers.serie import SerieSerializer


class AnSerializerComplete(serializers.ModelSerializer):
    serii = SerieSerializer(many=True, read_only=True)

    class Meta:
        model = An
        fields = ['id', 'num', 'facultate', 'serii']


class AnSerializer(serializers.ModelSerializer):
    class Meta:
        model = An
        fields = ['id', 'num', 'facultate', 'created', 'updated']
