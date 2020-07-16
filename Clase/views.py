from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
from Escuela.Clase.models import Clase
from Escuela.Clase.serializers import ClaseSerializer
from core.pagination import StandarResultsSetPagination


class ClaseViewSet(viewsets.ModelViewSet):
    queryset = Clase.objects.all()
    serializer_class = ClaseSerializer
    pagination_class = StandardResultsSetPagination