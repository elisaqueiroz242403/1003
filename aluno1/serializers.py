from rest_framework import serializers
from aluno1.models import Aluno
#from aluno1.serializers import AlunoSerializer

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ('__all__')
        