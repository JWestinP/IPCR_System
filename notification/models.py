from django.db import models
from django.contrib.auth.models import User, Group
# Create your models here.
class user_post (models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateField(null=True, blank=True)
    department = models.CharField(null=True, blank=True, max_length=255)
    new_post = models.CharField(null=True, blank=True, max_length=1000)
    
    