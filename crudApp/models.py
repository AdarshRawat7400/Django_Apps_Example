from django.db import models

# Create your models here.

class Position(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title

class Employee(models.Model):
    emp_code = models.CharField(max_length=5)  
    name = models.CharField(max_length=50)  
    email = models.EmailField()  
    contact = models.CharField(max_length=15)
    experience = models.IntegerField()
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
   