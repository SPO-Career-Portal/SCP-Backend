from django.db import models
import string
import random
import secrets

from placement.models import Placement
from intern.models import Intern
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
    password = models.CharField(max_length=20, null=True, blank=True, editable=False)
    activated = models.BooleanField(editable=False, default=False)
    placements_applied_for = models.ManyToManyField( Placement, editable=False, blank=True )
    interns_applied_for = models.ManyToManyField(Intern, editable=False, blank=True)
    verification_code = models.CharField(max_length=70, blank=True, null=True)
    
    def generate_verification_code(self):
        gen_code = "".join(
            secrets.choice(string.ascii_uppercase + string.digits) for i in range(28)
        )
        self.verification_code = gen_code
        self.save()
        return self.verification_code
    
    
    def __str__(self):
        return self.name
