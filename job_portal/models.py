from distutils.command.upload import upload
from inspect import modulesbyfile
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class userdetails(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    mobile=models.CharField(max_length=15,null=True)
    gender=models.CharField(max_length=5,null=True)
    type=models.CharField(max_length=15,null=True)
    
    def _str_(self):
        return self.user.username

class recruiter_details(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    mobile=models.CharField(max_length=15,null=True)
    type=models.CharField(max_length=15,null=True)
    company=models.CharField(max_length=50,null=True)   
    status=models.CharField(max_length=20,null=True)
    
    def _str_(self):
        return self.user.username
    
class jobs(models.Model):
    recruiter=models.ForeignKey(recruiter_details,on_delete=models.CASCADE)
    end_date=models.DateField()
    title=models.CharField(max_length=100)
    company=models.CharField(max_length=50)   
    salary=models.CharField(max_length=20)
    description=models.CharField(max_length=250)
    experience=models.CharField(max_length=100)
    skills=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    
    def _str_(self):
        return self.title
    

class applied(models.Model):
    job=models.ForeignKey(jobs,on_delete=models.CASCADE)
    candidate=models.ForeignKey(userdetails,on_delete=models.CASCADE)
    resume=models.FileField(null=True)
    applied_date=models.DateField()
     
    def _str_(self):
        return self.id