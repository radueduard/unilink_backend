from rest_framework import serializers
from ..Models.semigrupa import Semigrupa


class SemigrupaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semigrupa
        fields = ['id', 'nume', 'grupa']
