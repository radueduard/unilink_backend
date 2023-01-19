from rest_framework import serializers

from .grupa import GrupaSerializer
from .profesor import ProfesorSerializer
from .semigrupa import SemigrupaSerializer
from .serie import SerieSerializer
from ..Models.materie import Materie, Curs, Seminar, Laborator


class MaterieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materie
        fields = ['id', 'nume']
        abstract = True


class CursSerializer(MaterieSerializer):
    serie = SerieSerializer(many=False, read_only=True)

    class Meta(MaterieSerializer.Meta):
        model = Curs
        fields = MaterieSerializer.Meta.fields + ['profesor', 'serie']


class CursSerializerGET(MaterieSerializer):
    profesor = ProfesorSerializer(many=False, read_only=True)

    class Meta(MaterieSerializer.Meta):
        model = Curs
        fields = MaterieSerializer.Meta.fields + ['profesor']


class SeminarSerializer(MaterieSerializer):
    grupa = GrupaSerializer(many=False, read_only=True)

    class Meta(MaterieSerializer.Meta):
        model = Seminar
        fields = MaterieSerializer.Meta.fields + ['seminarist', 'grupa']


class SeminarSerializerGET(MaterieSerializer):
    seminarist = ProfesorSerializer(many=False, read_only=True)

    class Meta(MaterieSerializer.Meta):
        model = Seminar
        fields = MaterieSerializer.Meta.fields + ['seminarist']


class LaboratorSerializer(MaterieSerializer):
    semigrupa = SemigrupaSerializer(many=False, read_only=True)

    class Meta(MaterieSerializer.Meta):
        model = Laborator
        fields = MaterieSerializer.Meta.fields + ['asistent', 'semigrupa']


class LaboratorSerializerGET(MaterieSerializer):
    asistent = ProfesorSerializer(many=False, read_only=True)

    class Meta(MaterieSerializer.Meta):
        model = Laborator
        fields = MaterieSerializer.Meta.fields + ['asistent']
