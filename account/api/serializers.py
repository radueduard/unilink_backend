from rest_framework import serializers
from ..models import Account


class RegistrationSerializer(serializers.ModelSerializer):
    password_verify = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Account
        fields = ['email', 'username', 'password', 'password_verify']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        email = self.validated_data['email']
        username = self.validated_data['username']
        account = Account(
            email=email,
            username=username
        )
        password = self.validated_data['password']
        password_verify = self.validated_data['password_verify']

        if password != password_verify:
            raise serializers.ValidationError({'password': 'tre sa fie la fel'})

        account.set_password(password)
        account.save()
        return account
