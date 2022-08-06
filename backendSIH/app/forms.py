from django import forms
from .models import Document, Profile, Scheme


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = "__all__"

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'documentType': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'file': forms.FileInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control'}),
            'status': forms.TextInput(attrs={'class': 'form-control'}),
            'user': forms.Select(attrs={'class': 'form-control'}),
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"


class SchemeForm(forms.ModelForm):
    class Meta:
        model = Scheme
        fields = "__all__"
