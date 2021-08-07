from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=200)
    price = models.FloatField(default=0)
    quantity = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product-list')
