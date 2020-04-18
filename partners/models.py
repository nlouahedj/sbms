from django.db import models
from django.utils.translation import gettext_lazy as _


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


class Region(models.Model):
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


class Country(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    code = models.CharField(max_length=5, blank=False, null=False)

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=150, blank=False)
    zip_code = models.CharField(max_length=10, blank=False)
    region_id = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_('Region'))
    country_id = models.ForeignKey(Country, on_delete=models.PROTECT, blank=False, null=False,
                                   verbose_name=_('Country'))

    def __str__(self):
        return self.name


class Partner(models.Model):
    reference = models.CharField(max_length=10, unique=True, blank=False, null=False)
    name = models.CharField(max_length=150, blank=True, null=False)
    is_company = models.BooleanField(default=True)

    nrc = models.CharField(max_length=10, blank=True, null=True)
    nif = models.CharField(max_length=15, blank=True, null=True)
    nis = models.CharField(max_length=15, blank=True, null=True)
    nai = models.CharField(max_length=11, blank=True, null=True)

    SEX_CHOICES = [
        ('F', _('Female')),
        ('M', _('Male')),
        ('NA', _('Not specified')),
    ]
    sex = models.CharField(max_length=2, choices=SEX_CHOICES, default='NA')

    address1 = models.CharField(max_length=150, blank=True, null=True)
    address2 = models.CharField(max_length=150, blank=True, null=True)
    state_id = models.ForeignKey(State, on_delete=models.PROTECT, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)

    def full_address(self):
        return '{} {}\n{} - {}, {}'.format(
            self.address1,
            self.address2,
            self.zip_code,
            self.state_id,
            self.state_id.country_id)