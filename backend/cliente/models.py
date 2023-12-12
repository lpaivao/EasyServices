from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class Cliente(AbstractUser):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=20, unique=True, blank=True)
    password = models.CharField(max_length=128)
    rg = models.CharField(max_length=20, unique=True)
    cpf = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField()
    cep = models.CharField(max_length=10)
    endereco = models.CharField(max_length=255)
    numero_casa = models.CharField(max_length=10)
    cidade = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15, blank=True)
    
    groups = models.ManyToManyField(Group, related_name='cliente_groups', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='cliente_user_permissions', blank=True)
    
    
    def save(self, *args, **kwargs):
        # Garante que o username seja o mesmo que o email
        self.username = self.email
        super().save(*args, **kwargs)
    
    class Meta:
        db_table = 'cliente'
