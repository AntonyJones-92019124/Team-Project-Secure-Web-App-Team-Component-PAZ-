from django.contrib import admin

# Register your models here.

from .models import  Category, Project

"""Minimal registration of Models.
admin.site.register(Category)
admin.site.register(Project)
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

  #register Project.
  @admin.register(Project)
  #Project Admin class.
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
