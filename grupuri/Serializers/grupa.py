from rest_framework import serializers
from .semigrupa import SemigrupaSerializer
from ..Models.grupa import Grupa


class GrupaSerializerComplete(serializers.ModelSerializer):
    semigrupe = SemigrupaSerializer(many=True, read_only=True)

    class Meta:
        model = Grupa
        fields = ['id', 'num', 'serie', 'semigrupe']


class GrupaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grupa
        fields = ['id', 'num', 'serie', 'created', 'updated']
