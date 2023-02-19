from django.db import models
from django.shortcuts import reverse


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


