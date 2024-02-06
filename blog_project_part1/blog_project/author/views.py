from django.shortcuts import render, redirect
from . import forms
def add_author(request):
    if request.method == 'POST':
        author_form = forms.AuthorForm(request.POST)
        if author_form.is_valid(): # if the value is valid then save it in database
            author_form.save() # saving data in database
            return redirect('add_author') # return it to add_author
    else: #if user not passes data
        author_form = forms.AuthorForm()
    return render(request, 'add_author.html', {'form': author_form})

