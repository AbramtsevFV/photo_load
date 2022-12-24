from django import forms
from .models import Photo
from django.forms import FileInput

class ImageForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image', ]
        # widgets = {'image': FileInput(attrs={'class': 'btn btn-secondary'})
        # }