from django.contrib import admin
from .models import Products, Comment


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'active']


@admin.register(Comment)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['author', 'stars', 'product', 'active']
