from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    """
    Based on the UserManager of `django.contrib.auth.models`
    """

    user_in_migrations = True

    def create_user(self, email, password=None):

        user = self.model(
            email=self.normalize_email(email),
            is_active=True,
            is_staff=False,
            is_superadmin=False,
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None):
        user = self.model(
            email=self.normalize_email(email),
            is_active=True,
            is_staff=True,
            is_superadmin=True,
            is_superuser=True,
        )
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField("Correo electrónico", unique=True, blank=False)
    name = models.CharField(blank=False, verbose_name="Nombre")
    last_name = models.CharField(blank=False, verbose_name="Apellido")
    is_partner = models.BooleanField(default=False, verbose_name="Es colaborador")
    is_active = models.BooleanField(default=True, verbose_name="Está activo")
    is_staff = models.BooleanField(default=False, verbose_name="Es staff")
    is_superadmin = models.BooleanField(default=False, verbose_name="Es admin")
    is_superuser = models.BooleanField(default=False, verbose_name="Es super usuario")
    date_joined = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de registro",
    )

    objects = UserManager()

    USERNAME_FIELD = "email"

    class Meta:
        verbose_name = "Usuario"
