from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from products.models import Product
# Create your models here.

class Order(models.Model):
    order_date = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    email = models.EmailField()
    country = CountryField()
    phone = models.CharField(max_length=15)
    street_name = models.CharField(max_length=120)
    apartment_name = models.CharField(max_length=120)
    postal_code = models.CharField(max_length=8)
    city_name = models.CharField(max_length=100)
    stripe_pid = models.CharField(max_length=254, null=True, blank=True, default='')
    total = models.FloatField(null=True)
    
class OrderedItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField()
