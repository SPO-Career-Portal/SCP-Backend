from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=120)
    username = models.CharField(max_length=40, unique=True)
    roll = models.CharField(max_length=10, unique=True)
    batch = models.CharField(max_length=20)
    program = models.CharField(max_length=20)
    department = models.CharField(max_length=50)
    github = models.URLField(max_length=300, unique=True, null=True)
    linkedin = models.URLField(max_length=300, unique=True, null=True)
    mastercv = models.URLField(max_length=300, unique=True)
    resume1 = models.URLField(max_length=300, unique=True)
    resume2 = models.URLField(max_length=300, unique=True, null=True, blank=True)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=20, null=True, blank=True)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return self.name
