from django.db import models


class Brand(models.Model):
    abbreviation = models.CharField(max_length=10, unique=True, blank=False)
    name = models.CharField(max_length=150, blank=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    abbreviation = models.CharField(max_length=10, unique=True, blank=False)
    name = models.CharField(max_length=150, blank=False)
    parent = models.ForeignKey('self', on_delete=models.PROTECT, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    @property
    def depth(self):
        """Get depth"""
        p = self.parent
        if p:
            return 1 + p.depth
        else:
            return 0

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    reference = models.CharField(max_length=30, blank=False, unique=True)
    bar_code = models.CharField(max_length=100, blank=False, unique=True)
    name = models.CharField(max_length=100, blank=False)
    full_name = models.TextField(blank=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    # additional information
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, null=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=False)
    tags = models.ManyToManyField(Tag)
