from django.contrib import admin
from .models import Category, Product, Brand


class BrandAdmin(admin.ModelAdmin):
    list_display = ('abbreviation', 'name')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('abbreviation', 'name', 'parent')


# Register your models here.
admin.site.register(Brand, BrandAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product)
