from django.db import models

# Create your models here.
class Employee(models.Model):
    ename=models.CharField(max_length=20)
    eloc=models.CharField(max_length=20)

    def __str__(self):
        return self.ename