from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'ingredients', 'price', 'quantity')
    search_fields = ['name']


admin.site.register(Product, ProductAdmin)