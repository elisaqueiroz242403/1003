from django.shortcuts import render
from rest_framework import viewsets
from aluno1.models import Aluno
from aluno1.serializers import AlunoSerializer

from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = AlunoSerializer

    
        