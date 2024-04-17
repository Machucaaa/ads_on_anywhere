from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Propietario(AbstractUser):
    esta_activo = models.BooleanField(default=False)
    plan = models.IntegerField(default=365)
    fin_de_plan = models.DateField(auto_now=False,null=True)
    url = models.URLField(max_length=200) 
