from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Customuser(AbstractUser):
    CHOiCES = (
        (1,'admin'),
        (2,'User')
    )
    role = models.SmallIntegerField(default=1,choices=CHOiCES)
    phone = models.CharField(default='',max_length=20)