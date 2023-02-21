from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model


class Products(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    time_crated = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail_view', args=[self.pk])


class ActiveCommentManager(models.Manager):
    def get_queryset(self):
        return super(ActiveCommentManager, self).get_queryset().filter(active=True)


class Comment(models.Model):
    POINTS = [
        ('1', 'very bad'),
        ('2', 'bad'),
        ('3', 'normal'),
        ('4', 'good'),
        ('5', 'perfect'),
    ]
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    stars = models.CharField(max_length=10, choices=POINTS)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    object = models.Manager
    active_comment_manager = ActiveCommentManager()

    def get_absolute_url(self):
        return reverse('detail_view', args=[self.product.id])

