from django import forms
from .models import Document, Profile, Scheme
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


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


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2"
        ]


class CreateSchemeForm(forms.ModelForm):
    class Meta:
        model = Scheme
        fields = "__all__"


class CompleteProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"

class EditProfilePictureForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["img"]
