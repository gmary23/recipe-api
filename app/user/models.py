from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, # classe do django para os utilizadores
    BaseUserManager, 
    PermissionsMixin,
)
class UserManager(BaseUserManager): # responsável para administrar os usuários
    """Manager for users."""

    def create_user(self, email, password=None, **extra_fields): # extra_fields --> nomes ou outros campos
        """Create, save and return a new user."""
        if not email:
            raise ValueError("User must have an email address.")
        user = self.model(email=self.normalize_email(email), **extra_fields) # normalize_email -> transforma maiusculas em minusculas
        user.set_password(password)
        user.save(using=self._db) # guarda as informações na base de dados

        return user

    def create_superuser(self, email, password):
        """Create and return a new superuser."""
        user = self.create_user(email, password)
        user.is_staff = True # permissão 
        user.is_superuser = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin): # herda as propriedade da class # PermissionsMixin --> configura as permissões dos usuários
    """User in the system."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True) # estará ativado de imediato
    is_staff = models.BooleanField(default=False) # estará inativo

    objects = UserManager()

    USERNAME_FIELD = "email" # identificar único

