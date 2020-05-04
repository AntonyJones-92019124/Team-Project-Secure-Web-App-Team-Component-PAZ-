from django.db import models
from django.utils.text import slugify
from django.conf import settings
from django.urls import reverse
from django.db import models
# Create your models here.

#Categories class
class Category(models.Model):
  """Model representing a category."""
  category_name = models.CharField(max_length=100)
  category_description = models.CharField(max_length=200)
  full_description = models.TextField()
  author = models.CharField(max_length=100)

  class Meta:
      ordering = ['category_name', 'category_description', 'full_description']

  def get_absolute_url(self):
      """Returns the url to access a particular recipe instance."""
      return reverse('recipe_detail', args=[str(self.category_id)])

  def __str__(self):
      """String for representing the Model object."""
      return '{0}, {1}'.format(self.category_name, self.category_description)

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.CharField(max_length=20)
    full_description = models.TextField()
    image = models.FilePathField(path="/images")
