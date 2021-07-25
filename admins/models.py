from django.db import models


class Admin(models.Model):
    username = models.CharField(max_length=100, blank=False)
    password = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.username


# Create your models here.
