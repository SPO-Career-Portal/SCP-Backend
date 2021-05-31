import datetime

from django.db import models
from django.utils import timezone


class Placement(models.Model):
    placement_text = models.CharField(max_length=200)
    company = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    eligible_batches = models.JSONField(default= dict )
    eligible_branches = models.JSONField(default= dict )
    eligible_programes = models.JSONField(default= dict )
    deadline = models.DateTimeField('deadline')
    def __str__(self):
        return self.placement_text

