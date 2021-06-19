from django.db import models

# Create your models here.
from django.db import models
from intern.models import Intern
from placement.models import Placement
from user.models import User
import datetime

from hashlib import blake2b
from django.utils import timezone

# Create your models here.
class Registration(models.Model):
    defaultUser=User(name = 'Your Name',
    username = 'username',
    roll = 'roll',
    batch = 'batch',
    program = 'program',
    department = 'department',
    github = 'www.github.com',
    linkedin = 'www.linkedin.com',
    mastercv = 'www.google.com',
    resume1 = 'www.yahoo.com',
    resume2 = '',
    email = 'password',
    password ='',
    activated = False,)
    # eligibleForIntern=True,
    # eligibleForPlacement=False,)

    defaultIntern=Intern(intern_name = 'username',
    company ='company',
    duration = 'duration',
    role = 'role',
    description = 'description',
    eligible_batches = {'y19'},
    eligible_branches = {'y19'},
    eligible_programmes ={'y19'},
    deadline ='?date=2012-12-31T22:00:00.000Z',
    intern_start_month ='start_month',
    intern_end_month = 'end_month',
    key = '1',
    )
    defaultPlacement=Placement(
    placement_name = 'placement name',
    company = 'company',
    role = 'role',
    description = 'description',
    eligible_batches = {'y19'},
    eligible_branches ={'y19'},
    eligible_programmes = {'y19'},
    deadline = '?date=2012-12-31T22:00:00.000Z',
    key = '1',
    )

    user=models.ManyToManyField(User,blank=True,editable=True)
    isIntern=models.ManyToManyField(Intern,blank=True,editable=True)
    isPlacement=models.ManyToManyField(Placement,blank=True,editable=True)

    
   
    # user= models.ForeignKey(User, on_delete=models.CASCADE)

    # if(User.eligibleForPlacement):
    #     isIntern= models.ForeignKey(Intern, on_delete=models.CASCADE,editable=True,blank=True)
    # else:
    #     isPlacement= models.ForeignKey(User, on_delete=models.CASCADE,editable=True,blank=True)

    def __str__(self):
        return self.user

   