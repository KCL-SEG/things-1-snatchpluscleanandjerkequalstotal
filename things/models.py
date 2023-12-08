from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.

class Thing(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(blank=True, max_length=120)
    quantity = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])

    def clean(self):
        if self.description and len(self.description) > 120:
            raise ValidationError("Description must not have more than 120 characters")

        super().clean()

    def __str__(self):
        return self.name
