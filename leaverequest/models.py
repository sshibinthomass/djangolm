from django.db import models

# Create your models here.
class leaveDetails(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    phone=models.CharField(max_length=10)
    email=models.EmailField()
    regno=models.CharField(max_length=9)
    dept=models.CharField(max_length=3)
    year=models.CharField(max_length=15)
    reason=models.TextField()
    startDate=models.DateField(null=True)
    endDate=models.DateField(null=True)
    DateTime=models.DateTimeField(auto_now_add=True)