from django.db import models
from django.utils import timezone
# Create your models here.



JOB_TYPE = [
    ('Full time','Full time'),
    ('Part time','Part time'),
]

class Category(models.Model):
    name = models.CharField(max_length=25) 
    
    def __str__(self):
        return self.name

class Job(models.Model):
    title = models.CharField(max_length=50)
    #location
    job_type = models.CharField(max_length=50, choices = JOB_TYPE, default=1)
    description = models.TextField(max_length=1000, default=1)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title

