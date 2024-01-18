from django import forms
from django.forms import ModelForm
from .models import UploadImage


Create upload image form: 

class UploadImageForm(ModelForm):
    class Meta:
        model = UploadImage
        fields = ('Image',)