from django.db import models

# Create your models here.

class Aluno(models.Model):
    nome = models.CharField(
        max_length=50,
        verbose_name='Nome'
    )
    email = models.CharField(
        max_length=255,
        verbose_name='E-mail',
        unique=True
    )
    data_nascimento = models.CharField(
        max_length=50,
        verbose_name='Data de nascimento',
    )
    
    
    def __str__(self):
        return self.nome + '' + self.email



