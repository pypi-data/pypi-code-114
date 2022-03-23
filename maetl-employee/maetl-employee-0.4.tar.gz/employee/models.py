from django.db import models
from django.contrib.auth.models import User
from custom.models import *
import hashlib


class Employee(models.Model):
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    phone_number = models.IntegerField(blank=True, null=True)
    sex = models.CharField(choices=[(
        'Mane', 'Mane'), ('Feto', 'Feto')], max_length=6, null=True, blank=True)
    municipality = models.ForeignKey(
    Municipality, on_delete=models.CASCADE, null=True)
    administrativepost = models.ForeignKey(
    AdministrativePost, on_delete=models.CASCADE, null=True)
    village = models.ForeignKey(Village, on_delete=models.CASCADE, null=True)
    start_period = models.DateField(null=True, blank=True)
    end_period = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_end = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    datetime = models.DateTimeField(null=True)
    hashed = models.CharField(max_length=32, null=True)

    def save(self, *args, **kwargs):
        self.hashed = hashlib.md5(str(self.id).encode()).hexdigest()
        return super(Employee, self).save(*args, **kwargs)

    class Meta:
        ordering = ('-municipality',)

    def __str__(self):
        template = '{0.first_name} {0.last_name}'
        return template.format(self)

    class Meta:
        verbose_name_plural = 'Rejistu Dadus Empregu'


class EmployeeUser(models.Model):
    employee = models.OneToOneField(
        Employee, on_delete=models.CASCADE, related_name="employeeuser")
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        template = '{0.employee} {0.user}'
        return template.format(self)

    class Meta:
        verbose_name_plural = 'Dadus Empregu'
