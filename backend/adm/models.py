from django.db import models
from django.contrib.auth.models import AbstractUser
import random
from django.utils import timezone

class User(AbstractUser):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=20, unique=True, blank=True)
    password = models.CharField(max_length=128)
    rg = models.CharField(max_length=20, unique=True, blank=True, default=random.randint(1, 999))
    cpf = models.CharField(max_length=14, unique=True, blank=True, default=random.randint(1, 999))
    data_nascimento = models.DateField(blank=True, default=timezone.now)
    cep = models.CharField(max_length=10, blank=True)
    endereco = models.CharField(max_length=255, blank=True)
    numero_casa = models.CharField(max_length=10, blank=True)
    cidade = models.CharField(max_length=100, blank=True)
    bairro = models.CharField(max_length=100, blank=True)
    telefone = models.CharField(max_length=15, blank=True)
    
    USER_TYPE_CHOICES = [
        ('Cliente', 'Cliente'),
        ('Prestador', 'Prestador'),
    ]
    
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='Cliente')

    class Meta:
        db_table = 'user'