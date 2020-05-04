from django.urls import path
from django.urls import reverse
from django.contrib import admin
from . import views

urlpatterns = [
    #main Pages
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('categories', views.our_categories, name='our_categories'),
    #categories urls
    path('categories/', views.categories, name='categories'),
    path('view_categories/', views.view_categories, name='view_categories'),
    path('available_categories/', views.available_categories, name='available_categories'),
    #Register urls connected to Register class in views.py
    path('register/', views.Register.as_view(), name='register'),
    #Project Gallery urls
    path("project_index", views.project_index, name='project_index'),
    path("<int:pk>/", views.project_detail, name='project_detail'),
    #Category URLs#Project Gallery urls
    path("category_index", views.category_index, name='category_index'),
    path("category_detail/<int:id>/", views.category_detail, name='category_detail'),
]
