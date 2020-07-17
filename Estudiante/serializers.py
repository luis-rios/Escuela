from .models import Estudiante
from rest_framework import serializers


class BaseEstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = ['name']


class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = ['name', 'lastName', 'birth', 'clase']
