from django.db import models
import uuid

from users.models import Cook


# Create your models here.
class Recipe(models.Model):
    owner = models.ForeignKey(
        Cook, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=50)    
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, default='default.jpg')
    tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    
    
    # generic same for all
    created = models.DateField(auto_now_add=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    
    class Meta:
        ordering = ('created',)
    
    
    def __str__(self):
        return f'{self.title}, {self.created}'
    
    
class Tag(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name