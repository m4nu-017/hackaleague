from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
  user = models.ForeignKey(User, on_delete=models.SET_NULL , null = True , blank=True)
  employee_name = models.CharField(max_length=100)



class Employee(models.Model):
  user = models.ForeignKey(User, on_delete=models.SET_NULL , null = True , blank=True)
  full_name = models.CharField(max_length=100)
  email_id = models.EmailField()
  office_id = models.CharField(max_length=100)

    
