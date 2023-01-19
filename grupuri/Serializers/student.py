from rest_framework import serializers
from rest_framework import serializers

from .an import AnSerializer
from .facultate import FacultateSerializer
from .grupa import GrupaSerializer
from .semigrupa import SemigrupaSerializer
from .serie import SerieSerializer
from ..Models.grupa import Grupa
from ..Models.student import Student
from account.api.serializers import RegistrationSerializer


class StudentRegisterSerializer(RegistrationSerializer):

    class Meta(RegistrationSerializer.Meta):
        model = Student
        fields = RegistrationSerializer.Meta.fields + ['semigrupa']

    def save(self):
        email = self.validated_data['email']
        username = self.validated_data['username']
        semigrupa = self.validated_data['semigrupa']
        account = Student(
            email=email,
            username=username,
            semigrupa=semigrupa
        )
        password = self.validated_data['password']
        password_verify = self.validated_data['password_verify']

        if password != password_verify:
            raise serializers.ValidationError({'password': 'tre sa fie la fel'})

        account.set_password(password)
        account.save()
        return account


class StudentAllInfoSerializer(serializers.ModelSerializer):
    semigrupa = SemigrupaSerializer(many=False, read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'email', 'username', 'semigrupa']

