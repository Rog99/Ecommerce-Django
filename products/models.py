from django.db import models
from authentication.models import CustomUser

# Create your models here.


class ProductDetails(models.Model):
    PRODUCT_CHOICES = [
        ('BK', 'Books'),
        ('GE', 'Gym Equipments'),
        ('SA', 'Sports Accessories'),
        ('EE', 'Electronics')
    ]
    product_name = models.CharField(max_length=50, null=False, blank=False)
    product_path = models.CharField(max_length=100, null=False, blank=False)
    product_type = models.CharField(max_length=2, null=False, blank=False, choices=PRODUCT_CHOICES)
    price = models.IntegerField(null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    location = models.TextField(null=False, blank=False)
    user = models.ForeignKey('authentication.CustomUser', on_delete=models.SET_NULL, blank=True, null=True)


class ProductTags(models.Model):
    TAGS = [
        ('MB', 'Motivational Books'),
        ('DB', 'Defence Books'),
        ('CB', 'College Level Books'),
        ('NO', 'Novels')
    ]
    product_id = models.ForeignKey('ProductDetails', on_delete=models.SET_NULL, blank=True, null=True)
    tag = models.CharField(max_length=2, null=False, blank=False)
