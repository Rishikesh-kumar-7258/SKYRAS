from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Document, Scheme
from .forms import PostForm, RegisterForm, CreateSchemeForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .sendEmail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse


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
    template_name = "schemes/scheme.html"
    queryset = Scheme.objects.all()


class Help(TemplateView):
    template_name = "help.html"


class AboutUs(TemplateView):
    template_name = "aboutUs.html"


class ContactUs(TemplateView):
    template_name = "contactUs.html"


def show_what_is_happening(a, b):
    print(a, type(a))
    print(b, type(b))


# class CreateScheme(CreateView):
#     model = Scheme
#     form_class = CreateSchemeForm
#     template_name = "schemes/create.html"
#     success_url = "/"

#     # sending mails whenever a scheme is created
#     superusers_emails = User.objects.filter(
#         is_superuser=True).values_list('email')
#     receivers = [email[0] for email in list(superusers_emails)]
#     subject = "New scheme created"
#     body = "A new scheme is created please visit the website to know more"
#     # object_change = send_mail(receivers, subject, body)

# function based view to createscheme
def CreateScheme(request):

    if request.method == "POST":
        form = CreateSchemeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # sending mails whenever a scheme is created
            superusers_emails = User.objects.filter(
                is_superuser=True).values_list('email')
            receivers = [email[0] for email in list(superusers_emails)]
            subject = "New scheme created"
            body = "A new scheme is created please visit the website to know more"
            send_mail(receivers, subject, body)
            return redirect('homepage')
        else:
            return HttpResponse("Invalid form")
    else:
        form = CreateSchemeForm()
    return render(request, "schemes/create.html", {"form": form})
