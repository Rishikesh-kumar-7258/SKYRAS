from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Document, Scheme, Profile
from .forms import CompleteProfileForm, CreateDocumentForm, EditProfilePictureForm, LoginForm, RegisterForm, CreateSchemeForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
# from sms import send_sms


class HomePage(TemplateView):
    template_name = "home.html"


# Document related views
class viewDocument(LoginRequiredMixin, ListView):
    model = Document
    template_name = "document/viewDocuments.html"
    queryset = Document.objects.all()


class addDocument(LoginRequiredMixin, CreateView):
    model = Document
    form_class = CreateDocumentForm
    template_name = "document/addDocument.html"
    success_url = reverse_lazy("viewDocuments")

    def form_valid(self, form):
        app_model = form.save(commit=False)
        app_model.user = self.request.user
        app_model.save()
        return super().form_valid(form)


class verifyDocument(LoginRequiredMixin, UpdateView):
    model = Document
    template_name = "document/verifyDocument.html"
    fields = ['verified']
    success_url = '/'


class deleteDocument(LoginRequiredMixin, DeleteView):
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


class ProfileView(LoginRequiredMixin, TemplateView):
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

# function based view to createscheme


@login_required
def CreateScheme(request):

    if request.method == "POST":
        form = CreateSchemeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # sending mails whenever a scheme is created
            superusers_emails = User.objects.filter(
                is_superuser=True).values_list('email')
            # user_number = Profile.objects.all().values_list('phone_number')
            receivers = [email[0] for email in list(superusers_emails)]
            # phone_reciever = [phone[0] for phone in list(user_number)]
            subject = "New scheme created"
            body = "A new scheme is created please visit the website to know more"
            send_mail(subject, body, 'SKYRAS', receivers, fail_silently=False)
            # send_sms(body, "SKYRAS", phone_reciever, fail_silently=False)
            return redirect('homepage')
        else:
            return HttpResponse(form.errors)
    else:
        form = CreateSchemeForm()
    return render(request, "schemes/create.html", {"form": form})


# to create profile of the user
@login_required
def CompleteProfile(request):

    if request.method == "POST":
        form = CompleteProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("homepage")
        else:
            return HttpResponse("Invalid details")
    else:
        form = CompleteProfileForm()

    return render(request, "users/completeProfile.html", {"form": form})


@login_required
def EditProfileImage(request, pk):

    if request.method == "POST":
        profile = Profile.objects.filter(id=pk).first()
        print(profile.state)
        profile.img = request.FILES['img']
        profile.save()
        return redirect("profile")
    else:
        form = EditProfilePictureForm()
        return render(request, "users/editPic.html", {"form": form})


def Login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("homepage")
        else:
            return HttpResponse("Invalid credentials")

    form = LoginForm()
    return render(request, "users/login.html", {"form": form})
