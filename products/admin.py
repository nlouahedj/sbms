from django.contrib import admin
from admirarchy.toolbox import HierarchicalModelAdmin, AdjacencyList
from .models import Category, Product, Brand, Tag


class BrandAdmin(admin.ModelAdmin):
    list_display = ('abbreviation', 'name')
    list_filter = ('is_active', )
    search_fields = ('abbreviation', 'name')


class CategoryAdmin(HierarchicalModelAdmin):
    list_display = ('abbreviation', 'name', 'parent', 'is_active')
    list_filter = ('is_active', )
    autocomplete_fields = ('parent', )
    search_fields = ('abbreviation', 'name', 'parent__name', 'parent__abbreviation')
    hierarchy = True


class TagAdmin(admin.ModelAdmin):
    search_fields = ('name', )


class ProductAdmin(admin.ModelAdmin):
    list_display = ('reference', 'bar_code', 'name', 'brand', 'category')
    search_fields = ('reference', 'bar_code', 'name', 'full_name', 'description')
    autocomplete_fields = ('brand', 'tags', 'category')


# Register your models here.
admin.site.register(Brand, BrandAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Product, ProductAdmin)
