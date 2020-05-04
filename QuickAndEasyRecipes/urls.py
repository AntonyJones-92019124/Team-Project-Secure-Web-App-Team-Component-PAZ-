"""QuickAndEasyRecipes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from django.conf.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import reverse
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #categories urls connected to categories function in view.py file
    path('categories/', views.categories),
    path('view_categories/', views.view_categories),
    path('available_categories/', views.available_categories),
    path('delete_categories/<int:id>', views.delete_categories),
    #Gallery projects
    path('project_index/', views.project_index),
    path('project_detail/', views.project_detail),
    path("project_index", views.project_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
    #Categories URLs    path('project_index/', views.project_index),
    path('category_index/', views.category_index),
    path('category_detail/', views.category_detail),
    path("category_index", views.category_index, name="category_index"),
    path("category_detail/<int:id>/", views.category_detail, name="category_detail"),

]

urlpatterns += [
    path('home/', include('home.urls')),
]

urlpatterns += [
    path('', RedirectView.as_view(url='/home/')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
