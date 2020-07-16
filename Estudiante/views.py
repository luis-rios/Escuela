from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
from Escuela import Estudiante


class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.object.all()
    serializer_class = EstudianteSerializer
    pagination_class = StandarResultsSetPagination