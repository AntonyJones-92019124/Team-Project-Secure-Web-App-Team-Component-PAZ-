from django.shortcuts import render
from django.shortcuts import render, redirect
#import the class HttpResponse.
from django.http import HttpResponse
# for the try exception to work import Http404
from django.http import Http404
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from .models import Category, Recipe

#Add your function here

class Register(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'

def home(request):
    """View function for home page of site."""

    # Render the HTML template index.html with the data in the context variable.
    return render(
        request,
        'home.html',
        context={},
    )

def our_categories(request):
    """View function for categories page of site."""

    # Render the HTML template categories.html with the data in the context variable.
    return render(
        request,
        'categories.html',
        context={},
    )

def our_recipes(request):
    """View function for recipes page of site."""

    # Render the HTML template recipes.html with the data in the context variable.
    return render(
        request,
        'recipes.html',
        context={},
    )

from .forms import CategoriesForm
from .models import Category

#Category request function for Categories Form from forms.py
def categories(request):
    if request.method == "POST":
        form = CategoriesForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/view_categories')
            except:
                pass
    else:
        form = CategoriesForm()
    return render(request, 'create_categories.html',{'form':form})

#View categories Function
def view_categories(request):
    categories = Category.objects.all()
    return render(request, 'view_categories.html',{'categories':categories})

#availible categories function
def available_categories(request):
    categories= Category.objects.all()
    return render(request, 'available_categories.html',{'categories':categories})

#Delete a category Function
def delete_categories(request, id):
    categories = Category.objects.get(id=id)
    categories.delete()
    return redirect('/view_categories')

from .forms import RecipesForm
from .models import Recipe

#recipes request function for RecipesForm from forms.py
def recipes(request):
    if request.method == "POST":
        form = RecipesForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/view_recipes')
            except:
                pass
    else:
        form = RecipesForm()
    return render(request, 'create_recipes.html',{'form':form})

#View recipes Function
def view_recipes(request):
    recipes = Recipe.objects.all()
    return render(request, 'view_recipes.html',{'recipes':recipes})

#availible recipes function
def available_recipes(request):
    recipes= Recipe.objects.all()
    return render(request, 'available_recipes.html',{'recipes':recipes})

#Delete a recipe Function
def delete_recipes(request, id):
    recipes = Recipe.objects.get(id=id)
    recipes.delete()
    return redirect('/view_recipes')

from django.shortcuts import render
from home.models import Project

def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
     project = Project.objects.get(pk=pk)
     context = {
         'project': project
     }
     return render(request, 'project_detail.html', context)
