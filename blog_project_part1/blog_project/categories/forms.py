from django import forms
from .models import Category

class CategoryForm(forms.ModelForm):
    class Meta: # for including extra attributes in database
        model = Category
        fields = '__all__' # for including all fields of author