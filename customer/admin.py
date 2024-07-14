from django.contrib import admin
from . models import Customer_registration,Cart,Order,OrderDetail
# Register your models here.
admin.site.register(Customer_registration)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderDetail)


 