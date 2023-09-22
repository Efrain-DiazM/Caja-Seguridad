from rest_framework import serializers

from crear_clave_favorita.models import claveFavorita

class clave_serializer(serializers.ModelSerializer):
    class Meta:
        model =  claveFavorita
        fields = ['nombreClave', 'clave', 'confirmarClave', 'pista']
