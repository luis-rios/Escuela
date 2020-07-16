from rest_framework import serializers


class BaseClaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clase
        fields = ['name']


class ClaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clase
        fields = ['name', 'n_student', 'professor', 'schedule']