from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Book(models.Model):
    """
    Books data
    """
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=True)
    slug = models.SlugField(default="", null=False, db_index=True)  # if the title is Harry Potter 1 => the slug could be like this harry-potter-1
    
    def get_absolute_url(self):
        """To get url
        """
        # return reverse("book-detail", args=[self.id])
        return reverse("book-detail", args=[self.slug])
    
    def save(self, *args, **kwargs):
        """user defined save method.
        """
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    def __str__(self):
        """ format string to Return how ever we want
        """
        return f"{self.title} ({self.rating})"
