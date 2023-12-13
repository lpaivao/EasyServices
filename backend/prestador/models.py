from django.db import models
from django.contrib.auth import get_user_model

class Prestador(get_user_model()):
    antecedentes_criminais = models.FileField(upload_to='antecedentes_criminais/', blank=True)
    
    class Meta:
        db_table = 'prestador'