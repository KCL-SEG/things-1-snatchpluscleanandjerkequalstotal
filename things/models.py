from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.

class Thing(models.Model):
    name = models.CharField(max_length=30, unique=True, blank=False)
    description = models.TextField(blank=True, max_length=120)
    quantity = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])

    def clean(self):
        if not self.name:
            raise models.ValidationError("Name must not be blank")
        elif len(self.name) > 30:
            raise models.ValidationError("Name must consist of 30 characters or less")

        if self.description and len(self.description) > 120:
            raise models.ValidationError("Description must not have more than 120 characters")

        super().clean()

    def __str__(self):
        return self.name
