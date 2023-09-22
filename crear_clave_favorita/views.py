from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import clave_serializer
from .models import claveFavorita
import json

# Create your views here.

class ClaveFavoritaApiView(APIView):

    def get(self, request, *args, **kwargs):
        lista_clave_favoritas = claveFavorita.objects.all()
        serializador = clave_serializer(lista_clave_favoritas, many=True)
        return Response(serializador.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        data = {
            'nombreClave':request.data.get('nombreClave'),
            'clave':request.data.get('clave'),
            'confirmarClave':request.data.get('confirmarClave'),
            'pista':request.data.get('pista')
        }
        serializador = clave_serializer(data=data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data, status=status.HTTP_201_CREATED)
        else:
            print(serializador.errors)
            return Response(serializador.data, status=status.HTTP_400_BAD_REQUEST)