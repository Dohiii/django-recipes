from django.db import models
from django.contrib.auth.models import User
import uuid


# Create your models here.
class Cook(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    short_info = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(
        null=True, blank=True, upload_to='profiles/', default="profiles/user-default.png")
    
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.username)

class Skill(models.Model):
    owner = models.ForeignKey(
        Cook, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
   
    # generic same for all
    created = models.DateField(auto_now_add=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    
    def __str__(self):
        return f'Skill:   <{self.title}>  '