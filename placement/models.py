from django.db import models
from hashlib import blake2b
from django.utils import timezone


class Placement(models.Model):
    placement_name = models.CharField(max_length=300)
    company = models.CharField(max_length=300)
    role = models.CharField(max_length=100)
    description = models.TextField()
    eligible_batches = models.JSONField(default=list)
    eligible_branches = models.JSONField(default=list)
    eligible_programmes = models.JSONField(default=list)
    deadline = models.DateTimeField("deadline")
    key = models.CharField(max_length=20, editable=False, default=None)

    def save(self, *args, **kwargs):
        if self.key is None:
            timestamp = timezone.now()
            Hash = blake2b(digest_size=8)
            Hash.update(str(self.placement_name).encode())
            Hash.update(str(timestamp).encode())
            self.key = Hash.hexdigest()
        super(Placement, self).save(*args, **kwargs)

    def __str__(self):
        return self.placement_name
