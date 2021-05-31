from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=120)
    username=models.CharField(max_length=30, unique=True)
    batch=models.CharField(max_length=3)
    program=models.CharField(max_length=10)
    department=models.CharField(max_length=50)
    githubLink=models.URLField(max_length=100,unique=True,null=True)
    linkedinLink=models.URLField(max_length=200,unique=True,null=True)
    mastercv=models.URLField(max_length=300,unique=True)
    resume1=models.URLField(max_length=300,unique=True)
    resume2=models.URLField(max_length=300,unique=True,null=True,blank=True)


    def __str__(self):
        return self.name

