from django.shortcuts import render
from rest_framework import viewsets
from aluno1.models import Aluno
from aluno1.serializers import AlunoSerializer

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


    
        