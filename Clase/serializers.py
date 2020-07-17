from rest_framework import serializers

from Clase.models import Clase


class BaseClaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clase
        fields = ['name']


class ClaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clase
        fields = ['name', 'n_student', 'professor', 'schedule']