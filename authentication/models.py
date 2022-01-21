from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.forms import ModelForm

# Create your models here.


class CustomUser(AbstractBaseUser):
    full_name = models.CharField(max_length=50, null=False, blank=False)
    phone_number = models.BigIntegerField(
        null=False,
        blank=False,
        validators=[
            MinLengthValidator(10),
            MaxLengthValidator(10)
        ]
    )
    email = models.EmailField(null=False, blank=False, max_length=50, unique=True)
    password = models.CharField(null=False, blank=False, max_length=100)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'


