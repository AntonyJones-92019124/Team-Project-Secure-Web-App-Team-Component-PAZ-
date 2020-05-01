from django.contrib import admin

# Register your models here.

from .models import  Category, Recipe, Project

"""Minimal registration of Models.
admin.site.register(Category)
admin.site.register(Recipe)
admin.site.register(Image)
"""

#register Category.
@admin.register(Category)
#Category Admin class.
class CategoryAdmin(admin.ModelAdmin):
  """Administration object for Category models.
  Defines:
   - fields to be displayed in list view (list_display)
   - orders fields in detail view (fields),
     grouping the date fields horizontally
   - adds inline addition of tours in agent view (inlines)
  """
  list_display = ('category_name',
                  'category_description')
  fields = ['category_name', 'category_description']

  #register Recipes.
  @admin.register(Recipe)
  #Recipe Admin class.
  class RecipeAdmin(admin.ModelAdmin):
    """Administration object for Recipes models.
    Defines:
     - fields to be displayed in list view (list_display)
     - orders fields in detail view (fields),
       grouping the date fields horizontally
     - adds inline addition of tours in agent view (inlines)
    """
    list_display = ('recipe_name',
                    'recipe_steps')
    fields = ['recipe_name', 'recipe_steps']

  #register Recipes.
  @admin.register(Project)
  #Recipe Admin class.
  class ProjectAdmin(admin.ModelAdmin):
    """Administration object for Project models.
    Defines:
     - fields to be displayed in list view (list_display)
     - orders fields in detail view (fields),
       grouping the date fields horizontally
     - adds inline addition of tours in agent view (inlines)
    """
    list_display = ('title', 'description', 'author', 'image')
    fields = ['title', 'description','author', 'image']
