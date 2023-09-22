from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import login_serializer
from .models import logins
import json

# Create your views here.

class LoginApiView(APIView):

    def get(self, request, *args, **kwargs):
        lista_login = logins.objects.all()
        serializador = login_serializer(lista_login, many=True)
        return Response(serializador.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        data = {
            'nombreLogin':request.data.get('nombreLogin'),
            'email':request.data.get('email'),
            'usuario':request.data.get('usuario'),
            'contraseña':request.data.get('contraseña'),
            'url':request.data.get('url'),
            'nota':request.data.get('nota')
        }
        serializador = login_serializer(data=data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data, status=status.HTTP_201_CREATED)
        else:
            print(serializador.errors)
            return Response(serializador.data, status=status.HTTP_400_BAD_REQUEST)