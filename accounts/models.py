from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone


# Create your models here.
class Account(User, PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)
