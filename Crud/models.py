from django.db import models
from django.contrib.auth.models import AbstractUser
    
class User(AbstractUser): #AbstractUser te pone por default un formulario, aún así, puedo agregar más campos

    pass
