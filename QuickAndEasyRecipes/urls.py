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
    #Recipes urls connected to recipes function in views.property
    path('recipes/', views.recipes),
    path('view_recipes/', views.view_recipes),
    path('available_recipes/', views.available_recipes),
    path('delete_recipes/<int:id>', views.delete_recipes),
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