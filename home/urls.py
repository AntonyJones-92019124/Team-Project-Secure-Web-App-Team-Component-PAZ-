from django.urls import path
from django.urls import reverse
from django.contrib import admin
from . import views

urlpatterns = [
    #main Pages
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('categories', views.our_categories, name='our_categories'),
    path('recipes', views.our_recipes, name='our_recipes'),
    #categories urls
    path('categories/', views.categories, name='categories'),
    path('view_categories/', views.view_categories, name='view_categories'),
    path('available_categories/', views.available_categories, name='available_categories'),
    #recipes urls
    path('recipes/', views.recipes, name='recipes'),
    path('view_recipes/', views.view_recipes, name='view_recipes'),
    path('available_recipes/', views.available_recipes, name='available_recipes'),
    #Register urls connected to Register class in views.py
    path('register/', views.Register.as_view(), name='register'),
    #Project Gallery urls
    path("project_index", views.project_index, name='project_index'),
    path("<int:pk>/", views.project_detail, name='project_detail'),
]
