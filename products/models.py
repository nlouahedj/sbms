from django.db import models


class Brand(models.Model):
    abbreviation = models.CharField(max_length=10, unique=True, blank=False)
    name = models.CharField(max_length=150, blank=False)


class Category(models.Model):
    abbreviation = models.CharField(max_length=10, unique=True, blank=False)
    name = models.CharField(max_length=150, blank=False)
    parent = models.ForeignKey('self', on_delete=models.PROTECT)
    depth = models.IntegerField(default=0, blank=False)


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)


class Product(models.Model):
    reference = models.CharField(max_length=30, blank=False, unique=True)
    bar_code = models.CharField(max_length=100, blank=False, unique=True)
    name = models.CharField(max_length=100, blank=False)
    full_name = models.TextField()
    description = models.TextField()
    active = models.BooleanField(default=True)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, null=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=False)
