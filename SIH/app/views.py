from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Document
from .forms import PostForm, RegisterForm
from django.contrib.auth.models import User


class HomePage(TemplateView):
    template_name = "home.html"


# Document related views
class viewDocument(ListView):
    model = Document
    template_name = "document/viewDocuments.html"
    queryset = Document.objects.all()


class addDocument(CreateView):
    model = Document
    form_class = PostForm
    template_name = "document/addDocument.html"
    success_url = '/'


class verifyDocument(UpdateView):
    model = Document
    template_name = "document/verifyDocument.html"
    fields = ['verified']
    success_url = '/'


class deleteDocument(DeleteView):
    model = Document
    template_name = "document/deleteDocument.html"
    success_url = '/'


# url for signin
class SignIn(TemplateView):
    template_name = "users/signIn.html"

# urls for signup


class SignUp(CreateView):
    model = User
    form_class = RegisterForm
    template_name: str = "users/register.html"
    success_url = '/'


class FogotPassword(TemplateView):
    template_name: str = "users/forgotPassword.html"


class CompleteProfile(TemplateView):
    template_name: str = "users/completeProfile.html"


class Profile(TemplateView):
    template_name: str = "users/profile.html"
