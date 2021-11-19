from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('User is required !!')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        user = self.create_user(
            username=username,
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

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    objects = UserManager()
    USERNAME_FIELD = 'email'
