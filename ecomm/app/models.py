from operator import mod
from turtle import mode
from django.db import models
from sklearn.feature_extraction import image
from tables import Description
import datetime

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

            


class register(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    mobile = models.IntegerField()
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    gender = models.CharField(max_length=50)

    def __str__(self):
        return self.firstname

#static method
def getemail(email):
    try:
        return register.objects.get(email = email)
    except:
        return False    


class product(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to = 'upload/product')
    price = models.IntegerField(default= 100)
    description = models.CharField(max_length= 255,default="good")
    Category = models.ForeignKey(
        Category, on_delete=models.CASCADE, default = 1
    )

def __str__(self):
    return self.product

class order(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    customer = models.ForeignKey(register, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length= 50,default="",blank=True)
    phone = models.IntegerField()
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)   

