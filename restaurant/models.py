from django.db import models

# Create your models here.
class Restaurant_reg(models.Model):
    restname = models.TextField(max_length=100,null=True)
    restphone = models.TextField(max_length=100,null=True)
    restaddress = models.TextField(max_length=100,null=True)
    restemail = models.TextField(max_length=100,null=True)
    restpassword = models.TextField(max_length=100,null=True)

class Dishes(models.Model):
    dname = models.TextField(max_length=100,null=True)
    ddiscription = models.TextField(max_length=500,null=True)
    dprice = models.FloatField(null=True)
    dimage = models.ImageField(upload_to='dishes',null=True)
    drestaurant = models.ForeignKey(Restaurant_reg,on_delete=models.CASCADE,null=True)

