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
    tags        = models.ManyToManyField('Tag',blank=True)
    created    = models.DateTimeField(auto_now_add=True)
    #updated   = models.DateTimeField(auto_now=True)
    id         = models.UUIDField(default=uuid.uuid4,
                                  unique= True,primary_key=True,editable=False)

    # String representation projectobject
    
    def __str__(self):
        return self.Project_Name

class Review(models.Model):
 
    VOTE_TYPE = (
        ('up','up'),
        ('down','down')
        )

    #project = models.ForeignKey(Project,on_delete=models.CASCADE,
                                  #null=True,blank=True)
    # another apporach called related name
    project = models.ForeignKey(Project,on_delete=models.CASCADE,
                                         null = True, blank= True,related_name='reviews')

    body    = models.TextField(null=True,blank=True)
    value   = models.CharField(max_length=60,choices=VOTE_TYPE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    id      = models.UUIDField(default=uuid.uuid4,unique=True,
                                primary_key=True,editable=False)

    def __str__(self):
        return self.value

class Tag(models.Model):
    name = models.CharField(max_length= 200)
    id   = models.UUIDField(default=uuid.uuid4, unique = True,
                                    primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.name




