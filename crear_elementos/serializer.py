from rest_framework import serializers

from crear_elementos.models import logins, identificacion

class login_serializer(serializers.ModelSerializer):
    class Meta:
        model = logins
        fields = ['nombreLogin', 'email', 'usuario', 'contraseña', 'url', 'nota']

class identifiacion_serializer(serializers.ModelSerializer):
    class Meta:
        model = identificacion
        fields = ['nombreIdentificacion', 'numero', 'nombreCompleto', 'fechaNacimiento', 'fechaExpedicion', 'fechaVencimiento', 'nota']