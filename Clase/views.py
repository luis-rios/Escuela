from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
from Clase.models import Clase
from Clase.serializers import ClaseSerializer


class StandardResultsSetPagination(object):
    pass


class ClaseViewSet(viewsets.ModelViewSet):
    queryset = Clase.objects.all()
    serializer_class = ClaseSerializer
    pagination_class = StandardResultsSetPagination