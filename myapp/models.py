from django.db import models

# Create your models here.
class Customers(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField(max_length=10000)
    def __str__(self):
        return self.name