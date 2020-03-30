from rest_framework import serializers, viewsets
from .models import Cliente, Mascota, Paseador

class PaseadorProfileSerializer(serializers.ModelSerializer):
    usuario=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Paseador
        fields='__all__'

class PaseadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paseador 
        fields = ['idpas','nombre','apellido','direccion','rating','titulo','descripcion','foto']

class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = ['idmas','nombre','raza','edad','peso','sexo','tipo_mascota','foto','descripcion']

class ClientesSerializer(serializers.ModelSerializer):
    dueño=MascotaSerializer(many=True)
    class Meta:
        model = Cliente
        fields = ['idcli','nombre','apellido','direccion','telefono','correo','foto','dueño']
