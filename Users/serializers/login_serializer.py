from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from Users.models import User


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True, min_length=6)

    class Meta:
        model = User
        fields = ('email', 'password')

    def validate(self, attrs):
        if '@' not in attrs['email']:
            raise serializers.ValidationError('Correo electronico no tiene @')

        if any (domain in attrs['email'] for domain in [".ru", ".xyz"]):
            raise serializers.ValidationError("El dominio del correo no está permitidos")

        tiene_numero = any(letra.isdigit() for letra in attrs['password'])
        if not tiene_numero:
            raise serializers.ValidationError("La contraseña debe tener al menos un numero")

        user = User.objects.filter(email=attrs['email']).first()

        if not user:
            raise serializers.ValidationError("El usuario no existe")

        if not user.check_password(attrs['password']):
            raise serializers.ValidationError("Usuario o contraseña incorrecto")

        refresh = RefreshToken.for_user(user)
        refresh["username"] = user.username

        return{
            "success" : True,
            "data": {
                "refreshToken": str(refresh),
                "token": str(refresh.access_token),
                "email": user.email,
                "username": user.username
            }
        }

    
