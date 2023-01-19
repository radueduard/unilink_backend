from rest_framework import serializers

from ..Models.sala import Sala


class SalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sala
        fields = ['id', 'cladire', 'num']
