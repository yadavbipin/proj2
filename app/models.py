from django.db import models


class Product(models.Model):
    number = models.IntegerField(primary_key=True, max_length=4)
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    quantity = models.IntegerField(max_length=5)
