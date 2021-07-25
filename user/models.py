from django.db import models
import string
import random
import secrets
from django.utils import timezone

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
    github = models.URLField(max_length=300, unique=True, blank=True, null=True)
    linkedin = models.URLField(max_length=300, unique=True, blank=True, null=True)
    mastercv = models.URLField(max_length=300, unique=True, blank=True, null=True)
    resume1 = models.URLField(max_length=300, unique=True, blank=True, null=True)
    resume2 = models.URLField(max_length=300, unique=True, blank=True, null=True)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100, null=True, blank=True, editable=False)  
    activated = models.BooleanField(editable=False, default=False)
    placements_applied_for = models.ManyToManyField(
        Placement, editable=False, blank=True, through="PlacementResume"
    )
    interns_applied_for = models.ManyToManyField(
        Intern, editable=False, blank=True, through="InternResume"
    )
    verification_code = models.CharField(  
        max_length=70, blank=True, null=True, editable=False
    )

    def generate_verification_code(self):
        gen_code = "".join(
            secrets.choice(string.ascii_uppercase + string.digits) for i in range(28)
        )
        self.verification_code = gen_code
        self.save()
        return self.verification_code

    def __str__(self):
        return self.name


class PlacementResume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    placement = models.ForeignKey(Placement, on_delete=models.CASCADE, editable=False)
    resume = models.URLField(max_length=300, blank=False, editable=False)
    registered_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.registered_at = timezone.now()
        super(PlacementResume, self).save(*args, **kwargs)


class InternResume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    intern = models.ForeignKey(Intern, on_delete=models.CASCADE, editable=False)
    resume = models.URLField(max_length=300, blank=False, editable=False)
    registered_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.registered_at = timezone.now()
        super(InternResume, self).save(*args, **kwargs)
