from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


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
    email = models.EmailField(max_length=100, unique=True, null=False, blank=False)
    username = models.CharField(max_length=50, unique=True ,null=False, blank=False)

    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)

    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)


    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'users'
        ordering = ('-email',)
