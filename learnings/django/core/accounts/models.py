from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Student(models.Model):
    SHIRT_SIZES = (
        ('S','Small'),
        ('M','Medium')
    )
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()
    image = models.ImageField(null=True,blank=True)
    file = models.FileField(null=True,blank=True)
    date = models.DateField(null=True,blank=True)
    time = models.TimeField(null=True,blank=True)
    size = models.CharField(max_length=10,choices=SHIRT_SIZES,null=True,blank=True)