from django.db import models
from django.db.models.fields import GenericIPAddressField

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    grade = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_price = models.IntegerField()
    product_type = models.CharField(max_length=100)
    product_description = models.TextField()
    product_expiry_date = models.DateField()

    def __str__(self):
        return self.product_name
