from django.db import models


class Intern(models.Model):
    intern_name = models.CharField(max_length=500)
    company = models.CharField(max_length=500)
    duration = models.CharField(max_length=500)
    role = models.CharField(max_length=5000)
    description = models.CharField(max_length=5000)
    eligible_batches = models.JSONField(default=list)
    eligible_branches = models.JSONField(default=list)
    eligible_programs = models.JSONField(default=list)
    deadline = models.DateTimeField()
    intern_start_month = models.CharField(max_length=500)
    intern_end_month = models.CharField(max_length=500)

    def __str__(self):
        return self.intern_name
