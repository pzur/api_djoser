from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from .models import Cliente, Mascota, Paseador
from rest_framework import viewsets,permissions,authentication
from .serializer import ClientesSerializer,MascotaSerializer, PaseadorProfileSerializer, PaseadorSerializer

#Vistas de las tablas ha mostrar
class ClienteList(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClientesSerializer

class MascotaList(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer

class PaseadorList(viewsets.ModelViewSet):
    queryset = Paseador.objects.all()
    serializer_class = PaseadorSerializer

from rest_framework.generics import (ListCreateAPIView,RetrieveUpdateDestroyAPIView,)
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerProfileOrReadOnly

# Vista de todos los paseadores
class PaseadorProfileListCreateView(ListCreateAPIView):
    queryset=Paseador.objects.all()
    serializer_class=PaseadorProfileSerializer
    def perform_create(self, serializer):
        usuario=self.request.user
        serializer.save(usuario=usuario)

#Vista de un paseador en específico
class PaseadorProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Paseador.objects.all()
    serializer_class=PaseadorProfileSerializer
    permission_classes=[IsOwnerProfileOrReadOnly,IsAuthenticated]

from rest_framework import generics
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
import json

#Vista de Login para obtener token
from rest_framework.views import APIView
from django.contrib.auth import authenticate
class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            Token.objects.get_or_create(user=user)
            data = {"token": 'ola gente: ' +user.auth_token.key} 
        else:
            data = {"error": "No Son las Credenciales XD"}
        respuesta = json.dumps(data)
        return HttpResponse(respuesta,content_type='application/json')

# Vista Logout
class LogoutView(APIView):
    def get(self, request, format=None):
        # Borra el token
        request.user.auth_token.delete()
        return Response("Token borrado")
