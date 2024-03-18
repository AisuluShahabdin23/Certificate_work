from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email"]


class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField()

    class Meta:
        model = User
        fields = ['email', 'password', 'password2']

    def create(self, *args, **kwargs):
        user = User(email=self.validated_data['email'],
                    first_name=self.validated_data['email'],
                    last_name=self.validated_data['email'],
                    is_superuser=False,
                    is_staff=False,
                    is_active=True)
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({password: 'Passwords must match'})
        # Сохраняем пароль
        user.set_password(password)
        user.save()
        return user
