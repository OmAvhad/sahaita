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
    image = models.ImageField(upload_to='static/memories/', blank=True)
    date_posted = models.DateTimeField(default=datetime.now())
    alt_text = models.TextField(blank=True)