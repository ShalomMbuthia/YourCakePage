from django.db import models

# Create your models here.
class Customer(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.firstName+""+self.lastName

class CakesAndEquipments(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    description = models.TextField()
    origin = models.CharField(max_length=50,default="Kenya")
    color = models.CharField(max_length=30,default="white")

    def __str__(self):
        return self.name
