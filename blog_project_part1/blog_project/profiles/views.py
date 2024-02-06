from django.shortcuts import render, redirect
from . import forms
def add_profile(request):
    if request.method == 'POST':
        profile_form = forms.ProfileForm(request.POST) # getting user post request data here
        if profile_form.is_valid(): # if the value is valid then save it in database
            profile_form.save() # saving data in database
            return redirect('add_profile') # return it to add_author
    else: #if user not passes data then they'll find blank form
        profile_form = forms.ProfileForm()
    return render(request, 'add_profile.html', {'form': profile_form})

