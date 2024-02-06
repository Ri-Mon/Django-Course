from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta: # for including extra attributes in database
        model = Post
        fields = '__all__' # for including all fields of author