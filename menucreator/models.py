from django.db import models
from django.contrib.auth.models import User


class Menu(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, null=False, on_delete=models.SET(1))

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.TextField()
    max_quantity = models.IntegerField(null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)

    def __str__(self):
        return self.name


class MenuCategory(models.Model):
    name = models.CharField(max_length=200)
    menu_items = models.ManyToManyField(MenuItem)
    menu = models.ManyToManyField(Menu)

    def __str__(self):
        return self.name


