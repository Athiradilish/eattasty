from django.db import models
from restaurant.models import *

# Create your models here.
class Customer_registration(models.Model):
    name = models.TextField(max_length=100,null=True)
    email = models.EmailField(max_length=100,null=True)
    number = models.TextField(max_length=100,null=True)
    password = models.TextField(max_length=100,null=True)
    address = models.TextField(max_length=300,null=True)

class Cart(models.Model):
    dish = models.ForeignKey(Dishes,on_delete=models.CASCADE,null=True)
    restaurant = models.ForeignKey(Restaurant_reg,on_delete=models.CASCADE,null=True)
    customer = models.ForeignKey(Customer_registration,on_delete=models.CASCADE,null=True)
    quantity = models.PositiveBigIntegerField(default=1)
class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected')
    ]

    customer = models.ForeignKey(Customer_registration, on_delete=models.CASCADE,null=True)
    total_price = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES, default='Pending',null=True)
    order_date =  models.DateTimeField(auto_now_add=True,null=True)
    dish_detail = models.ForeignKey(Cart,on_delete=models.CASCADE,null=True)
    restaurant_detail = models.ForeignKey(Restaurant_reg,on_delete=models.CASCADE,null=True)


# def __str__(self):
#     return self.customer.name
    
class OrderDetail(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,null=True)
    dish = models.ForeignKey(Dishes,on_delete=models.CASCADE,null=True)
    restaurant = models.ForeignKey(Restaurant_reg,on_delete=models.CASCADE,null=True)
    quantity = models.PositiveIntegerField()



 