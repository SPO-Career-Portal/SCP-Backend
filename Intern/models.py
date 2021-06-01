from django.db import models

class Intern_Data(models.Model):
    Intern_Name = models.CharField(max_length = 500)
    Company = models.CharField( max_length = 500)
    Duration = models.CharField( max_length=500)
    Role = models.CharField( max_length = 5000)
    Description = models.CharField( max_length = 5000)
    Eligible_Batches = models.JSONField( default = list)
    Eligible_Branches = models.JSONField( default = list)
    Eligible_Programs = models.JSONField( default = list)
    Deadline = models.DateTimeField()
    Intern_Start_Month = models.CharField( max_length = 500)
    Intern_End_Month = models.CharField( max_length = 500)
    def __str__(self):
        return self.Intern_Name
# Create your models here.
