from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('User is required !!')
        user = self.model(email=email)
        user.document = 0
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=email,
            password=password
        )
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    id_usu = models.BigAutoField(primary_key=True)
    name = models.CharField('Nombre', max_length=40, null=False)
    lastName = models.CharField('Apellidos', max_length=40, null=False)
    document = models.IntegerField('Documento')
    email = models.CharField('Email', max_length=100, unique=True)
    password = models.CharField('clave', max_length=256, null=False)
    cellphone = models.CharField('Telefono', max_length=25)

    @property
    def is_staff(self):
        return self.is_superuser

    def save(self, **kwargs):
        super().save(**kwargs)

    objects = UserManager()
    USERNAME_FIELD = 'email'
