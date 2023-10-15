from django.db import models
from django.contrib.auth.models import User
from datetime import datetime 

# Create your models here.
class UserInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    
    
class UserMood(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mood = models.CharField(max_length=500, null=True, blank=True)
    date = models.DateField()
    

class Memories(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    date_posted = models.DateTimeField(default=datetime.now())
    alt_text = models.TextField(blank=True)
    

class Medications(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=500, null=True, blank=True)
    time_of_day = models.TimeField(null=True, blank=True)
    
    
class MedicationsRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medications, on_delete=models.CASCADE)
    taken = models.BooleanField(default=False)
    date = models.DateField(null=True, blank=True)
    
    
class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.CharField(max_length=500, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    location = models.CharField(max_length=500, null=True, blank=True)
    reason = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    

class Location(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    date_time = models.DateTimeField()