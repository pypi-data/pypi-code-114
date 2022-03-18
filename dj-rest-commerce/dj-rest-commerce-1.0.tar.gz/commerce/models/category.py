from django.db import models
from commerce.models.core import CoreEntity


class Category(CoreEntity):
    name = models.CharField(max_length=70, unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='parentCategory')
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='category/%y/%m', blank=True, null=True)

    def __str__(self):
        return self.name


class Model(CoreEntity):
    name = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Brand(CoreEntity):
    name = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='brand/%y/%m', blank=True, null=True)

    def __str__(self):
        return self.name


class Tag(CoreEntity):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
