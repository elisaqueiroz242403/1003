from django.shortcuts import render

from rest_framework import viewsets
from professor.models import Professor
from professor.serializer import ProfessorSerializer

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import TokenAuthentication


class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    permision_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = ProfessorSerializer


