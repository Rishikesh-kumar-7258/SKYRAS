from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Document, Scheme
from .forms import PostForm, RegisterForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy


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



class SignUp(CreateView):
    model = User
    form_class = RegisterForm
    template_name: str = "users/register.html"
    success_url = reverse_lazy('login')

# url for resetting password


class FogotPassword(TemplateView):
    template_name: str = "users/forgotPassword.html"

# url for completing the profile page


class CompleteProfile(TemplateView):
    template_name: str = "users/completeProfile.html"

# url to go to profile page


class Profile(TemplateView):
    template_name: str = "users/profile.html"


class Schemes(ListView):
    model = Scheme
    template_name = "scheme.html"
    queryset = Scheme.objects.all()


class Help(TemplateView):
    template_name = "help.html"


class AboutUs(TemplateView):
    template_name = "aboutUs.html"


class ContactUs(TemplateView):
    template_name = "contactUs.html"
