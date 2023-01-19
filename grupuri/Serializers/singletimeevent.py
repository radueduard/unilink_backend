from rest_framework import serializers

from .materie import CursSerializer
from ..Models.singletimeevent import Tema, Examen


class TemaSerializer(serializers.ModelSerializer):
    curs = CursSerializer(many=False, read_only=True)

    class Meta:
        model = Tema
        fields = ['id', 'curs', 'title', 'description', 'due_date']


class ExamenSerializer(serializers.ModelSerializer):
    curs = CursSerializer(many=False, read_only=True)

    class Meta:
        model = Examen
        fields = ['id', 'curs', 'title', 'description', 'tip', 'date']
