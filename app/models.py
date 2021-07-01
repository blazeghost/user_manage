from django.db import models
from datetime import *

# Create your models here.


class Master_Table(models.Model):
    Email = models.EmailField(max_length=50)
    Password = models.CharField(max_length=50)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_created = models.DateTimeField(auto_now_add=True)


class User(models.Model):
    m_id = models.ForeignKey(Master_Table, on_delete=models.CASCADE)
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Role = models.CharField(max_length=50)
    allow_create = models.BooleanField(default=True)
    allow_delete = models.BooleanField(default=True)
    allow_edit = models.BooleanField(default=True)


class Table_one(models.Model):
    a_id = models.ForeignKey(User, on_delete=models.CASCADE)
    visitor_name = models.CharField(max_length=50)
    visitor_purpose = models.CharField(max_length=50)
    visitor_contact = models.CharField(max_length=50)
    concerned_person = models.CharField(max_length=50)
    date_time = models.DateTimeField(blank=True)


class Table_two(models.Model):
    s_id = models.ForeignKey(User, on_delete=models.CASCADE)
    tableone_id = models.ForeignKey(Table_one, on_delete=models.CASCADE)
    visitor_address = models.CharField(max_length=100)
    visitor_vehicle_number = models.CharField(max_length=50)
