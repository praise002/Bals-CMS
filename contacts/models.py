from django.db import models
from django.utils import timezone
from rest_framework import generics
from django_countries.fields import CountryField

class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    message = models.TextField()
    country_code = CountryField()
    created = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return self.full_name


