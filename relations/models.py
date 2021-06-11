from django.db import models


class City(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    type = models.CharField(max_length=50)  # noqa: A003
    manufacturer = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.type


class Client(models.Model):
    city = models.ForeignKey(City, models.SET_NULL, blank=True, null=True)
    products = models.ManyToManyField(Product)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)

    def __str__(self):
        return self.first_name


class Supplier(models.Model):
    city = models.OneToOneField(City, models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
