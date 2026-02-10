from django.db import models
from product.models.category import Category


class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)

    category = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.title