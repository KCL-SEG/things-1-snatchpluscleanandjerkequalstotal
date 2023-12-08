from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.

class Thing(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(blank=True, max_length=120)
    quantity = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
