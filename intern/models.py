from django.db import models
from hashlib import blake2b
from django.utils import timezone


class Intern(models.Model):
    intern_name = models.CharField(max_length=500)
    company = models.CharField(max_length=500)
    duration = models.CharField(max_length=500, default="", blank=True)
    role = models.TextField()
    description = models.TextField()
    eligible_batches = models.JSONField(default=list)
    eligible_branches = models.JSONField(default=list)
    eligible_programmes = models.JSONField(default=list)
    deadline = models.DateTimeField()
    intern_start_month = models.CharField(max_length=500, default="", blank=True)
    intern_end_month = models.CharField(max_length=500, default="", blank=True)
    key = models.CharField(max_length=20, editable=False, default=None)

    def save(self, *args, **kwargs):
        if self.key is None:
            timestamp = timezone.now()
            Hash = blake2b(digest_size=8)
            Hash.update(str(self.intern_name).encode())
            Hash.update(str(timestamp).encode())
            self.key = Hash.hexdigest()
        super(Intern, self).save(*args, **kwargs)

    def __str__(self):
        return self.intern_name
