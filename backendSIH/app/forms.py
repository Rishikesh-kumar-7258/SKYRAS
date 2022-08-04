from django import forms
from .models import Document, Profile, Scheme


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = "__all__"


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"

class SchemeForm(forms.ModelForm):
    class Meta:
        model = Scheme
        fields = "__all__"