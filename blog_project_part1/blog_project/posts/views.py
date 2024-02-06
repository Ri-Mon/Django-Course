from django.shortcuts import render, redirect
from . import forms, models

def add_post(request):
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST) # getting user post request data here
        if post_form.is_valid(): # if the value is valid then save it in database
            post_form.save() # saving data in database
            return redirect('add_post') # return it to add_post
    else: #if user not passes data then they'll find blank form
        post_form = forms.PostForm()
    return render(request, 'add_post.html', {'form': post_form})


def edit_post(request, id):
    post = models.Post.objects.get(pk=id) # getting post id as it is the primary key
    #print(post.title)
    post_form = forms.PostForm(instance = post) # for getting existing post contents in edit form

    if request.method == 'POST':
        post_form = forms.PostForm(request.POST, instance = post) # getting user post request data here and if user make no change then the content remains unchanged(instance = post)
        if post_form.is_valid(): # if the value is valid then save it in database
            post_form.save() # saving data in database
            return redirect('homepage') # return it to add_post

    return render(request, 'add_post.html', {'form': post_form})

def delete_post(request, id):
    post = models.Post.objects.get(pk=id) # getting post id as it is the primary key
    post.delete()

    return redirect('homepage')

