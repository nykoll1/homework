from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    birth_date = models.DateField()

    def __str__(self):
        return self.user.username