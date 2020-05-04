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

from .models import Category, Project

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

#Project functions
from django.shortcuts import render
from home.models import Project

#Project functions
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

#category functions
from django.shortcuts import render
from home.models import Category

#category functions
def category_index(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'category_index.html', context)

def category_detail(request, id):
     category = Category.objects.get(id=id)
     context = {
         'category': category
     }
     return render(request, 'category_detail.html', context)
