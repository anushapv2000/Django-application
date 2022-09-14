from django.db import models

# Create your models here.
class library(models.Model):
    userid=models.AutoField(primary_key=True)
    bookname=models.CharField(max_length=400)
    username=models.CharField(max_length=400)
    issuedate=models.DateField()
#class admin(models.Model):
#    userid=models.AutoField(primary_key=True)
#    username=models.CharField(max_length=400)

#    issuedate=models.DateField()