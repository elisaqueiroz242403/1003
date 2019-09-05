from django.db import models

# Create your models here.

class Professor(models.Model):
    nome = models.CharField(
        max_length=50,
        verbose_name='Nome'
    )
    idade = models.CharField(
        max_length=50,
    )
    email = models.EmailField(
        max_length=50,
    )


    
    def __str__(self):
        return self.nome + '' + self.email

