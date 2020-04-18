from django.contrib import admin

from .models import Country, Category, Region, Partner, State

admin.site.register(Category)
admin.site.register(Region)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(Partner)