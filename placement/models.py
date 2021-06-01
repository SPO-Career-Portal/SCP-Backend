from django.db import models

class Placement(models.Model):
    placement_text = models.CharField(max_length=300)
    company = models.CharField(max_length=300)
    role = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    eligible_batches = models.JSONField(default= list )
    eligible_branches = models.JSONField(default= list )
    eligible_programes = models.JSONField(default= list )
    deadline = models.DateTimeField('deadline')
    def __str__(self):
        return self.placement_text

