from django import forms
from .models import Document, Profile, Scheme, SchemeRegistration, SchemeTracking
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from captcha.fields import CaptchaField

SCHEME_CATEGORY = (
    ('GEN', "General"),
    ('OBC', "Other Backward Caste"),
    ('SC', "Scheduled Caste"),
    ('ST', "Scheduled Tribe"),
)

SCHEME_GENDER = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
)


class CreateDocumentForm(forms.ModelForm):

    captcha = CaptchaField()

    class Meta:
        model = Document
        fields = (
            "name",
            "file",
            "captcha"
        )


class RegisterForm(UserCreationForm):

    captcha = CaptchaField()

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
            "captcha"
        ]


class CreateSchemeForm(forms.ModelForm):
    captcha = CaptchaField()
    # category = forms.MultipleChoiceField(
    #     choices=SCHEME_CATEGORY, widget=forms.CheckboxSelectMultiple())
    # gender = forms.MultipleChoiceField(
    #     choices=SCHEME_GENDER, widget=forms.CheckboxSelectMultiple())

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


class LoginForm(forms.ModelForm):

    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ["username", "password", "captcha"]


class SchemeRegistrationForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = SchemeRegistration
        fields = "__all__"


class SchemeTrackingCreateForm(forms.ModelForm):
    class Meta:
        model = SchemeTracking
        fields = "__all__"
