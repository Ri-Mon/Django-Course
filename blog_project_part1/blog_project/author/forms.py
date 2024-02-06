from django import forms
from .models import Author

class AuthorForm(forms.ModelForm):
    class Meta: # for including extra attributes in database
        model = Author
        fields = '__all__' # for including all fields of author
        # fields = ['name', 'bio']
        # exclude = ['bio']