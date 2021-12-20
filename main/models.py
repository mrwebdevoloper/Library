from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser



class Users(AbstractUser):
    birthday = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    is_client = models.BooleanField(default=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    photo = models.ImageField(null=True, blank=True, upload_to='users')


    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'


class Category(models.Model):
    name = models.CharField(max_length=234)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=225)
    prise = models.IntegerField(null=True, blank=True)
    photo = models.ImageField(upload_to='products')
    pdf = models.FileField(upload_to='product')
    muallif = models.CharField(max_length=500)

    def __str__(self):
        return self.name