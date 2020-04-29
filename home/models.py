from django.db import models

# Create your models here.

from django.urls import reverse

#Categories class
class Category(models.Model):
  """Model representing a category."""
  category_name = models.CharField(max_length=100)
  category_description = models.CharField(max_length=2500)

  class Meta:
      ordering = ['category_name', 'category_description']
      db_table = "home_categories"

  def get_absolute_url(self):
      """Returns the url to access a particular recipe instance."""
      return reverse('recipe_detail', args=[str(self.category_id)])

  def __str__(self):
      """String for representing the Model object."""
      return '{0}, {1}'.format(self.category_name, self.category_description)


#Recipe class
class Recipe(models.Model):
  """Model representing a Recipe."""
  recipe_name = models.CharField(max_length=100)
  recipe_steps = models.CharField(max_length=2500)

  class Meta:
      ordering = ['recipe_name', 'recipe_steps']
      db_table = "home_recipes"

  def get_absolute_url(self):
      """Returns the url to access a particular recipe instance."""
      return reverse('recipe_detail', args=[str(self.id)])

  def __str__(self):
      """String for representing the Model object."""
      return '{0}, {1}'.format(self.recipe_name, self.recipe_steps)
