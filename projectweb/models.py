from hashlib import blake2s
from turtle import title
from django.db import models
import uuid

# Create your models here.
class Project(models.Model):
    # owner
    Project_Name = models.CharField(max_length=200)
    Description = models.TextField(null=True,blank=True)
    # feature_image = model
    demo_link  = models.CharField(max_length=1000,null=True,blank=True)
    source_link = models.CharField(max_length=1000,null=True,blank=True)
    vote_total = models.IntegerField(default=0)
    vote_ratio = models.IntegerField(default=0)
    created    = models.DateTimeField(auto_now_add=True)
    id         = models.UUIDField(default=uuid.uuid4,
                                  unique= True,primary_key=True,editable=False)

    # String representation projectobject
    
    def __str__(self):
        return self.Project_Name



