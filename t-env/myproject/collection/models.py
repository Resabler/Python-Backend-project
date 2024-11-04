from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import EmailValidator
class Employee(models.Model):
   
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50,blank=False)
    email=models.EmailField(unique=True,validators=[EmailValidator()])
    department=models.CharField(max_length=100,
                                choices=[
                                    ('HR','HR'),('Sales','Sales'),('Engineering','Engineering')
                                ],blank=True
                                )
    role=models.CharField(max_length=100,
                          choices=[('Manager','Manager'),('Developer','Developer'),('Analyst','Analyst')],
                          blank=True
                          )
    date_joined=models.DateTimeField(default=timezone.now)
    
     

