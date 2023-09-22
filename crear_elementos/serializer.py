from rest_framework import serializers

from crear_elementos.models import logins

class login_serializer(serializers.ModelSerializer):
    class Meta:
        model = logins
        fields = ['nombreLogin', 'email', 'usuario', 'contraseña', 'url', 'nota']