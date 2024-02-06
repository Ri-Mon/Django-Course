from django.shortcuts import render, redirect
from . import forms
def add_category(request):
    if request.method == 'POST':
        category_form = forms.CategoryForm(request.POST)
        if category_form.is_valid(): # if the value is valid then save it in database
            category_form.save() # saving data in database
            return redirect('add_category') # return it to add_author
    else: #if user not passes data
        category_form = forms.CategoryForm()
    return render(request, 'add_category.html', {'form': category_form})

