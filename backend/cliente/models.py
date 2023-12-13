from django.db import models
from django.contrib.auth.models import AbstractUser

class Cliente(AbstractUser):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Renomeado para seguir a convenção do Django
    rg = models.CharField(max_length=20, unique=True)
    cpf = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField()
    cep = models.CharField(max_length=10)
    endereco = models.CharField(max_length=255)
    numero_casa = models.CharField(max_length=10)
    cidade = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15, blank=True)
    
    class Meta:
        db_table = 'cliente'