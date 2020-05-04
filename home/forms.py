from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime  # for checking renewal date range.

from django import forms
from .models import Category

#Category Form class.
class CategoriesForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
