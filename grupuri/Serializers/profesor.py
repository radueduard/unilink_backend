from rest_framework import serializers
from ..Models.profesor import Profesor
from account.api.serializers import RegistrationSerializer


class ProfesorRegisterSerializer(RegistrationSerializer):

    class Meta(RegistrationSerializer.Meta):
        model = Profesor
        fields = RegistrationSerializer.Meta.fields + ['tip']

    def save(self):
        email = self.validated_data['email']
        username = self.validated_data['username']
        tip = self.validated_data['tip']
        account = Profesor(
            email=email,
            username=username,
            tip=tip
        )
        password = self.validated_data['password']
        password_verify = self.validated_data['password_verify']

        if password != password_verify:
            raise serializers.ValidationError({'password': 'tre sa fie la fel'})

        account.set_password(password)
        account.save()
        return account


class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = ['id', 'email', 'username']
