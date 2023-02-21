from django.contrib import admin
from .models import Products, Comment


class ProductCommentInline(admin.TabularInline):
    model = Comment
    fields = ['author', 'stars', 'body', 'active']


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'active']
    inlines = [ProductCommentInline,]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'stars', 'product', 'active']
