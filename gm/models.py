from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Exercise(models.Model):
    photo = models.ImageField(upload_to="r")
    Exe_name = models.CharField(max_length=50)
    Exe_time=models.CharField(max_length=50,default=0)

    def __str__(self)->str:
        return self.Exe_name
    

class Pro(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    img=models.ImageField(upload_to="r")   
    # name=models.CharField(max_length=50) 
    


