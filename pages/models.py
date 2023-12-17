from django.db import models
from account.models import Account


class Product(models.Model):
    host = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=25)
    brand = models.CharField(max_length=25, blank=True)
    image = models.ImageField(upload_to="product/images")
    price = models.FloatField()
    quantity = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name + " " + self.category
