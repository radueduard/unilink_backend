from rest_framework import serializers
from ..Models.facultate import Facultate
from ..Serializers.an import AnSerializer


class FacultateSerializerComplete(serializers.ModelSerializer):
    ani = AnSerializer(many=True, read_only=True)

    class Meta:
        model = Facultate
        fields = ['id', 'num', 'name', 'ani']


class FacultateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facultate
        fields = ['id', 'num', 'name', 'created', 'updated']
