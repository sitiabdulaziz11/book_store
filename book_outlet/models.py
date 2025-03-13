from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Book(models.Model):
    """
    Books data
    """
    title = models.CharField(max_length=50)
    rating = models.IntegerField()
    
    def __str__(self):
        """ format string to Return how ever we want
        """
        return f"{self.title} ({self.rating})"