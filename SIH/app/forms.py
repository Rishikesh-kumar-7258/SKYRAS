from django import forms
from .models import Document


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
