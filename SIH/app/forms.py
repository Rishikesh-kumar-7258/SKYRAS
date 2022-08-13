from django import forms
from .models import Document
from django.contrib.auth.models import User


class PostForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = (
            "name",
            "description",
            "file",
        )

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'file': forms.FileInput(attrs={'class': 'form-control'}),
        }


class RegisterForm(forms.ModelForm):

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password"
        )
