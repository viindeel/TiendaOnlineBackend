from typing import Self

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.text import slugify

NOT_ALLOWED_DOMAIN = [".ru", ".xyz"]

class UserManager(BaseUserManager):
    def create_user(self, email = None, password = None, **extra_fields):
        if not email:
            raise ValueError("El correo electronico no puede estar vacio")

        if "@" not in email:
            raise ValueError("El correo no es valido")

        if any(domain in email for domain in NOT_ALLOWED_DOMAIN):
            raise ValueError("El dominio del correo no es valido")

        if not password:
            raise ValueError("La contraseña no puede estar vacia")

        if len(password) < 6:
            raise ValueError("La contraseña debe tener al menos 6 caracteres")

        if not any(caracter.isdigit() for caracter in password ):
            raise ValueError("La contraseña debe tener al menos un digito")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)



class User(PermissionsMixin, AbstractBaseUser):
    email = models.EmailField(max_length=100, unique=True, null=False, blank=False, verbose_name="Correo Electónico", help_text="(Obligatorio")
    username = models.CharField(max_length=50, unique=True ,null=False, blank=False, help_text="(Obligatorio")

    first_name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Nombre", help_text="(Obligatorio")
    last_name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Apellidos", help_text="(Obligatorio")

    is_superuser = models.BooleanField(default=False, verbose_name="¿Es Super Usuario?")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True, verbose_name="¿Está Activo?")

    role = models.ForeignKey("Role", on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Rol de usuario", help_text="(Obligatorio)")


    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'users'
        ordering = ('-email',)
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'


def save(self, *args, **kwargs):
    if not self.username:
        self.username = f"{slugify(self.first_name)}-- {slugify(self.last_name)}--{self.email[:3].upper()}"
    super().save(*args, **kwargs)

    def __str__(self):
        nombre = f"{self.first_name}{self.last_name}" if self.first_name and self.last_name else "DESCONOCIDO"
        return f"{nombre}({self.email})"

    def get_full_name(self):
        nombre = f"{self.first_name} {self.last_name}" if self.first_name and self.last_name else "DESCONOCIDO"
        return f"{nombre}"