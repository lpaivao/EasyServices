from django.db import models
from django.contrib.auth import get_user_model

class Cliente(get_user_model()):
    
    class Meta:
        db_table = 'cliente'
