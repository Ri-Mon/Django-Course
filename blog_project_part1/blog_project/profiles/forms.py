from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta: # for including extra attributes in database
        model = Profile
        fields = '__all__' # for including all fields of author
        # fields = ['name', 'bio']
        # exclude = []