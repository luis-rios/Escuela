from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
from .models import Estudiante
from Clase.views import StandardResultsSetPagination
from .serializers import EstudianteSerializer


class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer
    pagination_class = StandardResultsSetPagination