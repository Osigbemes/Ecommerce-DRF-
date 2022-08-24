from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class CustomAccountManager(BaseUserManager):

    def create_superuser(self, username, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(username, password, **other_fields)

    def create_user(self, username, password, **other_fields):

        if not username:
            raise ValueError(_('You must provide a username'))

        user = self.model(username=username, **other_fields)
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):

    userName= models.CharField(max_length=200, unique=True)
    firstName = models.CharField(max_length=200, blank=True, null=True)
    objects = CustomAccountManager()
    USERNAME_FIELD = 'userName'
    REQUIRED_FIELDS = ['firstName']
